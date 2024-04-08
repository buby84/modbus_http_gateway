#machine.py
from ctypes import addressof
from operator import itemgetter
import datetime

from pyModbusTCP.constants import EXP_SLAVE_DEVICE_BUSY 
#import config
from re import X
from models import Log, LogJobs
#from . import db

class Machine:

    def __init__(self,bluprint_regs,bluprint_regs_calc) -> None:

        self.__regs = {
        }

        self.__regs_calc = {
        }

        self.__alarmsDescriptions = {            
        }


        self.__commandQueuee = []
        self.__commandResult = []


        self.__logDB = []
        self.__logJobDB = []

        self.__bluprint_regs = bluprint_regs
        self.__bluprint_regs_calc = bluprint_regs_calc

        #self.__bluprint_regs = config.modbus_regs
        #self.__bluprint_regs_calc = config.modbus_regs_calc

        #populate regs with default values

        for key,item in self.__bluprint_regs.items():
            self.__regs[key] = 0 
            self.__bluprint_regs[key] = self.__setRegDefValues(item)
            
        for key,item in self.__bluprint_regs_calc.items():
            self.__regs_calc[key] = 0
            self.__bluprint_regs_calc[key] = self.__setRegDefValues(item)


    @property
    def blueprints(self):
        blueprints = {**self.__bluprint_regs, **self.__bluprint_regs_calc}
        return blueprints

    @property
    def regiters(self):
        regs = {**self.__regs, **self.__regs_calc}
        return regs

    @property
    def alarmsDescriptions(self):
        alarmsDescriptions= {}
        for key,item in self.__bluprint_regs.items():
            if "emergenza" in item:
                alarmsDescriptions[key] = item
        for key,item in self.__bluprint_regs_calc.items():
            if "emergenza" in item:
                alarmsDescriptions[key] = item
        return alarmsDescriptions

    @property
    def commandQueuee(self):
        return self.__commandQueuee
        
    @property
    def commandResult(self):
        #reverse array        
        return self.__commandResult


    def __setRegDefValues(self, blueprint):

        if ("log" not in blueprint):
            blueprint['log'] = True
        if ("tag" not in blueprint):
            blueprint['tag'] = "---"
        if ("plcaddr" not in blueprint):
            blueprint['plcaddr'] = "#---"
        if ("display" not in blueprint):
            blueprint['display'] = True
        return blueprint




    
    #change value of a register
    #return yes if been changed
    def __setRegistry(self, registry, value):
        
        if registry in self.__regs:
            
            blueprint = self.__bluprint_regs[registry]  

            #check if differenct and log
            if self.__regs[registry] != value:
                self.__regs[registry] = value 
                self.__log(registry, value,blueprint)
            
            return True

        else:
            #reg not defined
            return False
    

    #calculate registry
    def __calcRegs(self):

        for key,item in self.__regs_calc.items():
            value = key,self.__regs_calc[key] 
            #TO-DO: add control if exist 


            blueprint = self.__bluprint_regs_calc[key]
            valuetype = blueprint['valuetype']


            #decode value       
            #time
            #print(key)
            if valuetype == "time":
                my_formatter = "{:02d}"
                hour = self.__regs[ blueprint['regs_main_hour'] ]
                minutes = self.__regs[ blueprint['regs_main_minute'] ]
                value =  my_formatter.format(hour) + ":" + my_formatter.format(minutes)
            #multibit   
            elif valuetype == "bit": 
                bit_mask = {
                    0  : 0b0000000000000001,
                    1  : 0b0000000000000010,
                    2  : 0b0000000000000100,
                    3  : 0b0000000000001000,
                    4  : 0b0000000000010000,
                    5  : 0b0000000000100000,
                    6  : 0b0000000001000000,
                    7  : 0b0000000010000000,
                    8  : 0b0000000100000000,
                    9  : 0b0000001000000000,
                    10 : 0b0000010000000000,
                    11 : 0b0000100000000000,
                    12 : 0b0001000000000000,
                    13 : 0b0010000000000000,
                    14 : 0b0100000000000000,
                    15 : 0b1000000000000000,
                }
                bit = blueprint['bit']
                reg_main = blueprint['regs_main'] 
                #print(key)                
                #print(reg_main)
                value = 1 if self.__regs[ reg_main ] & bit_mask[bit] else 0
            
            elif valuetype == "char":                 
                reg_main = blueprint['regs_main'] 
                reg_count = blueprint['regs_count'] 
                value = ""
                for x in range(0,reg_count):
                    reg_calc = reg_main + x
                    value_to_decode = self.__regs[ reg_calc ]
                    value2 = chr(   ((value_to_decode >> 8) & 0xff) )
                    value1 = chr(   (value_to_decode  & 0xff ) )
                    value = value + value1 + value2 
                value = value.split(" ")[0]        
                #print(value)   


            
            #check if differenct and log
            if value != self.__regs_calc[key]:
                self.__regs_calc[key] = value  #set value in registry
                self.__log(key,self.__regs_calc[key],blueprint)
            

    #load all data from a dictionary
    def load(self,regs):    
        for key, value in regs.items():
            modified = self.__setRegistry(key,value)
        
        self.__calcRegs()
        self.__logJob()

        #after


    # add the log to the database
    def __log(self, registry,value,blueprint):
        
        if  blueprint['log']:


            log = {
                'registry' : registry,
                'value' : value
            }
            self.__logDB.append(log) 

            '''
            new_log = Log(code=registry, value=value)
            from flask import Flask
            from flask_sqlalchemy import SQLAlchemy
            app = Flask(__name__)
            #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'                
            app.config['SQLALCHEMY_DATABASE_URI'] = config.app['db_uri']
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.app['db_track_modification']
            db = SQLAlchemy()
            db.init_app(app)
            with app.app_context():
                db.session.add(new_log)
                db.session.commit()
            '''
    
    def getNextLogDB(self):
        if len(self.__logDB)==0:
            return False
        else:
            log = self.__logDB[0] 
            self.__logDB.pop(0)
            return log


            
    # add the log to the database
    def __logJob(self):
        
        program = self.__regs[4513]
        product = self.__regs_calc[20110000]

        workingtime_hour = self.__regs[8034]
        workingtime_minutes = self.__regs[8033]
        
        status_exec = self.__regs_calc[20100003] == 1
        status_end = self.__regs_calc[20100002] == 1
        
        #controlli
        #programma non impostato
        if program==0:
            return False

        status = 0
        if status_end :
            status = 10
        elif status_exec:
            status = 1

        #print('STATO::')
        #print(status)

        workingtime = datetime.time(workingtime_hour,workingtime_minutes,0)

        log = {
            'program' : program,
            'product' : product,
            'time' : workingtime,
            'status' : status,
        }

        toinsert = True

        
        for idx, val in enumerate(self.__logJobDB):
            if self.__logJobDB[idx]['product'] == product:
                self.__logJobDB[idx] = log
                toinsert = False
        
        #print('toinsert::')
        #print(toinsert)

        if toinsert:
            self.__logJobDB.append(log) 

            
        #print(self.__logJobDB)

    def getNextLogJobDB(self):
        if len(self.__logJobDB)==0:
            return False
        else:
            log = self.__logJobDB[0] 
            self.__logJobDB.pop(0)
            return log


    # add to the queuee the command to execute
    def addCommand(self, commandType, address, value=0 ):
        if address>=0 and address <= 65535:
            command = {
                'commandType' : commandType,
                'address' : address,
                'value' : value,
            }
            self.__commandQueuee.append(command) 
            return True
        else:
            return False

        

    # get and remove next command
    def getNextCommand(self ):
        if len(self.__commandQueuee)==0:
            return False
        else:
            command = self.__commandQueuee[0] 
            self.__commandQueuee.pop(0)
            return command

            
    # add to the queuee the command to execute
    def addCommandResult(self, command, result  ):
        command["result"] = result
        command["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__commandResult.append(command)
        #keep last 10 logs only
        self.__commandResult = self.__commandResult[-10:] 
        return True

        
    # add to the queuee the command to execute
    def setBarcode(self, barcode ):
        import struct
        barcode = str(barcode)
        barcode = barcode.ljust(20,' ')
        
        #print(barcode)
        if len(barcode)<=20:
            #if len(barcode) % 2: barcode += '\x00' #if odd add void  att he end
            #if len(barcode) % 2: barcode += ' ' #if odd add void  att he end
            split_strings = [None] * 10
            n  = 2
            x = 0
            #split sting ing roup of 2
            for index in range(0, len(barcode), n):
                split_strings[x] = (barcode[index : index + n])
                x += 1
            print("split string")
            print(split_strings)
            for index in range(0, 10):
                #print(index)
                address = 20110 +index
                value = split_strings[index]
                #print(value)
                if value is not None:
                    value = struct.unpack("<h",bytes(value, encoding='utf8'))[0] #convert in ascii
                    #print(value)
                print(address)
                print(value)
                self.addCommand(commandType=49,address=address,value=value)

            return True
        else:
            return False