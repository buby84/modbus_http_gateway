# init.py
from config import registers,registers_calc

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from sqlalchemy.sql import select
from sqlalchemy.sql.expression import null

import time
from threading import Thread, Lock
from pyModbusTCP.client import ModbusClient
import pickle
import configparser
import os

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
from machine import Machine
from models import Log,LogJobs


regs_lock = Lock()
regs_lock = Lock()
lmac = Machine(registers.regs,registers_calc.regs)

config_ini = configparser.ConfigParser()
config_ini.read(os.path.join(os.path.dirname(__file__), 'config', 'main.ini'))
secret_key = config_ini['APP']['secretkey']
db_uri = config_ini['DB']['uri']
db_track = config_ini['DB']['track_modification'] == 1

loginenabled =  config_ini['APP']['login'] == 1

pooling_time = int(config_ini['MODBUS']['pooling_time'])
host = config_ini['MODBUS']['host']
port = int(config_ini['MODBUS']['port'])
debug = config_ini['MODBUS']['debug'] == 1
auto_open = config_ini['MODBUS']['auto_open'] == 1

# modbus polling thread
def polling_th_read():
    global lmac
    

    client = ModbusClient(host=host ,port=port, debug=debug, auto_open=auto_open)

    # polling loop
    while True:
        # keep TCP open
        if not client.is_open():
            client.open()


        #read 
        regs = {}
        for key in lmac.regiters.keys():          
            if key < 65536: #if more than 65k mean is a splitted value so no need to read
                try : 
                    #regtoread = item['regs']
                    #regtoread = lmac.blueprints[key]['regs']
                    regtoread = key
                    reg_list = client.read_holding_registers(regtoread, 1)
                    # if read is ok, store result in regs (with thread lock synchronization)
                    if reg_list:
                        with regs_lock:
                            regs[key] = list(reg_list)[0]

                except Exception as e:
                    print("polling_th_read error")
                    print(e)
                    pass

        with regs_lock:
            lmac.load(regs)

        # 1s before next polling
        time.sleep(pooling_time)
        
        
# modbus polling thread
def polling_th_commands():
    global lmac

    client = ModbusClient(host=host ,port=port, debug=debug, auto_open=auto_open)

    # polling loop
    while True:
        # keep TCP open
        if not client.is_open():
            client.open()
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = secret_key
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = db_track
        db.init_app(app)

        log = lmac.getNextLogDB()
        while log != False:
            try : 
                new_log = Log(code=log['registry'], value=log['value'])
                
                
                with app.app_context():
                    db.session.add(new_log)
                    db.session.commit()
                    
            except Exception as e:
                print("polling_th_commands error log 1")
                print(e)
            log = lmac.getNextLogDB()

  
        job = lmac.getNextLogJobDB()
        while job != False:
            try : 
                with app.app_context():


                    program = job['program']
                    product = job['product']
                    workingtime = job['time']
                    status = job['status']


                    #LogJobs.autocomplete_other(product=product)

                    #autcomplete different 
                    LogJobs.query.filter(LogJobs.product!=product).update({"status":10})

                    new_log = LogJobs.query.filter(LogJobs.product==product).first() # 
                    if new_log: # if a log
                        new_log.time = workingtime
                        new_log.status =status
                        #print('job aggiornato')
                    else:
                        new_log = LogJobs(program=program, product=product, time=workingtime, status=status)
                        db.session.add(new_log)
                        #print('job aggiunto')
                    db.session.commit()
            
                    
            except Exception as e:
                print("polling_th_commands error log 2")
                print(e)
            job = lmac.getNextLogJobDB()


        command = lmac.getNextCommand()
        while command != False:
            try : 
                commandType = int(command['commandType']) 
                address = int(command['address'])
                value = int(command['value'])
                commandResult = False
                #read register
                if commandType == 40:
                    reg_list = client.read_holding_registers(address, 1) 
                    # if read is ok, store result in regs (with thread lock synchronization)
                    if reg_list:
                        commandResult = list(reg_list)[0]

                #write register
                elif commandType == 49:
                    commandResult = client.write_single_register(address, value) 
                    

                lmac.addCommandResult(command,commandResult)
            except Exception as e:
                print("polling_th_commands error command")
                print(e)
            
            command = lmac.getNextCommand()

                    
        #print(lmac.regiters)


        time.sleep(pooling_time)
    #client.close();

def create_app():
    #global app
    #global db

    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = db_track
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for non-auth parts of app
    from api import api as api_blueprint
    app.register_blueprint(api_blueprint)




    # new thread ? 
    # start polling thread
    tp = Thread(target=polling_th_read)
    # set daemon: polling thread will exit if main thread exit
    tp.daemon = True
    tp.start()

    # new thread ? 
    # start polling thread
    tp_2 = Thread(target=polling_th_commands)
    # set daemon: polling thread will exit if main thread exit
    tp_2.daemon = True
    tp_2.start()


    return app



