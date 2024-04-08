# main.py

from flask import Blueprint, json, render_template, redirect, url_for, request, flash
from flask import request
from flask_login import login_required, current_user
from flask import jsonify
from config import registers, registers_calc
from models import Log, LogJobs
from app import lmac

api = Blueprint('api', __name__)


#commands
@api.route('/machine/commands/todo/get')
def command_queuee_get():
    regs = lmac.commandQueuee
    return jsonify(regs)

@api.route('/machine/commands/todo/put', methods=['POST'])
def command_queuee_put():

    commandType = request.json["commandType"]
    address = request.json["address"]
    value = request.json["value"]

    result = lmac.addCommand(commandType=commandType, address=address, value=value)

    return jsonify(result)




@api.route('/machine/barcode/put', methods=['POST'])
def barcode_put():
    print("CHANGE BARCODE")
    print(request)
    print(request.json)
    barcode = request.json["barcode"]
    result = lmac.setBarcode(barcode=barcode)

    return jsonify(result)    
    
@api.route('/machine/commands/result/get')
def command_result_get():
    regs = lmac.commandResult
    return jsonify(regs)

    
@api.route('/machine/get-status')
def get_status():
    regs = lmac.regiters
    return jsonify(regs)

@api.route('/machine/blueprints/get')
def get_blueprints():
    regs = lmac.blueprints
    return jsonify(regs)




#logs
@api.route('/machine/get-logs')
def get_logs():

    logs = Log.query.order_by(Log.id.desc()).all()
    json_list=[i.serialize for i in logs]
    for idx, log in enumerate(json_list):
        json_list[idx]['plcaddr'] = ""
        json_list[idx]['tag'] = ""
        json_list[idx]['descrizione'] = ""
        json_list[idx]['value_raw'] = json_list[idx]['value']
        
        bluprint= False
        if log["code"] in  registers.regs : 
            bluprint = registers.regs[log["code"]]
        if log["code"] in  registers_calc.regs : 
            bluprint = registers_calc.regs[log["code"]]

        if bluprint != False :
            json_list[idx]['plcaddr'] = bluprint['plcaddr'] 
            json_list[idx]['tag'] = bluprint['tag'] if ("tag" in bluprint) else ""
            json_list[idx]['descrizione'] = bluprint['descrizione'] if ("descrizione" in bluprint) else "" 
            #decodifca valore
            #if ("values" in bluprint) and (log['value'] in bluprint['values']) : 
            #    json_list[idx]['value'] = bluprint[log['value']]



    return jsonify(json_list)

@api.route('/machine/get-logJobs')
def get_logJobss():

    logs = LogJobs.query.order_by(LogJobs.id.desc()).all()
    json_list=[i.serialize for i in logs]
    for idx, log in enumerate(json_list):
        json_list[idx]['status_raw'] = json_list[idx]['status']
        if json_list[idx]['status_raw'] == 0 :
            json_list[idx]['status'] = "Pausa"
        elif json_list[idx]['status_raw'] == 1 :
            json_list[idx]['status'] = "Esecuzione"
        elif json_list[idx]['status_raw'] == 10 :
            json_list[idx]['status'] = "Completato"


    return jsonify(json_list)
    

@api.route('/machine/export/status-xls')
def export_status_xls():
    return jsonify(lmac.regiters)

@api.route('/machine/export/logs-xls')
def export_log_xls():
    return jsonify(lmac.regiters)