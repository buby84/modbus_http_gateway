# main.py

from flask import Blueprint, render_template, abort, redirect, url_for
from flask_login import login_required, current_user
from flask import jsonify
from flask import request
from models import Log, LogJobs
from app import lmac,loginenabled

main = Blueprint('main', __name__)



@main.route('/')
def index():
    
    log = Log()
    log.delete_expired_logs()
    
    #check if is logged and redirect to dashboard    
    if loginenabled & (not current_user.is_authenticated):
        return render_template('login.html')
    else:
        alarmsDescriptions = lmac.alarmsDescriptions
        blueprints = lmac.blueprints
        return render_template('dashboard/index.html', pageName="Home", alarmsDescriptions = alarmsDescriptions, blueprints = blueprints)


@main.route('/logs')
def logs():#check if is logged and redirect to dashboard    
    if loginenabled & (not current_user.is_authenticated):
        return render_template('login.html')
    else:
        return render_template('dashboard/logs.html', pageName="Logs")

@main.route('/logJobs')
def logJobs():#check if is logged and redirect to dashboard    
    if loginenabled & (not current_user.is_authenticated):
        return render_template('login.html')
    else:
        return render_template('dashboard/logJobs.html', pageName="LogJobs")


@main.route('/modbus')
def modbus():#check if is logged and redirect to dashboard    
    if loginenabled & (not current_user.is_authenticated):
        return render_template('login.html')
    else:
        return render_template('dashboard/modbus.html', pageName="Modbus")

@main.route('/config')
def config():#check if is logged and redirect to dashboard    
    if loginenabled & (not current_user.is_authenticated):
        return render_template('login.html')
    else:
        import configparser
        import os
        config_ini = configparser.ConfigParser()
        config_ini_path = os.path.join(os.path.dirname(__file__), 'config', 'main.ini')
        config_ini.read( config_ini_path )
        return render_template('dashboard/config.html', pageName="Configurazione", config_ini = config_ini)

        
@main.route('/config/save', methods=['POST'])
def config_save():#check if is logged and redirect to dashboard    

    login = "1" if request.form.get('login') == "on" else "0"
    day_retention_logs = str(request.form.get('day_retention_logs'))
    day_retention_logsJob = str(request.form.get('day_retention_logsjob'))
    host = request.form.get('modbus_host')
    port = str(request.form.get('modbus_port'))
    pooling_time = str(request.form.get('modbus_pooling_time'))

    
    import configparser
    import os
    config_ini = configparser.ConfigParser()
    config_ini_path = os.path.join(os.path.dirname(__file__), 'config', 'main.ini')
    config_ini.read( config_ini_path )
    print(login)
    config_ini['APP']['login'] = login
    config_ini['LOGS']['day_retention_logs'] = day_retention_logs
    config_ini['LOGS']['day_retention_logsJob'] = day_retention_logsJob
    config_ini['MODBUS']['host'] = host
    config_ini['MODBUS']['port'] = port
    config_ini['MODBUS']['pooling_time'] = pooling_time

    with open(config_ini_path, 'w') as configfile:    # save
        config_ini.write(configfile)
        print("file main.ini edited "+config_ini_path)

    return redirect(url_for('main.config'))