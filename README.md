# General

This project implements an easy interface , logger, and a gateway to http api rest for modbus protocol

# Content

The file *Simple_ModbusServer.py* contains the code for a simple Modbus Server with the following register description:

| Holding Register Addr. | Description |
| --- | --- |
| 0 | Server writes a random value to it every 500 ms |
| 1 | Server monitors this register for changes. If the value is changed by the client, the server will print out the new value |

# Configuration 

To run the script, you need to have pyModbusTCP installed on your machine. To install it, you can use:


pip3 install virtualenv

pip3 install pyModbusTCP flask flask-sqlalchemy flask-login pyyaml

#linux
~~~~
sudo apt install python3
sudo apt install python3-pip
pip3 install virtualenv
sudo pip3 install pyModbusTCP  flask flask-sqlalchemy flask-login pyyaml
~~~~


# Configuration files

this files must be editd 
config/main.ini
contain general info about modbus and the webapp

config/registes.py
contain list of registers and description of modbus


# Creare venv di sviluppo
python -m venv venv   oppure sudo virtualenv venv 
 
# Attivare venv
.\venv\Scripts\activate 
oppure  
source venv/bin/activate 

installare i moduli pyton



- windows 
set FLASK_ENV=development
$env:FLASK_ENV = "development"

- linux
export FLASK_ENV=development


# Run

flask run

o accessibile dal esterno
flask run --host=0.0.0.0 




    

# Deploy

https://stackoverflow.com/questions/33586346/start-python-flask-webserver-automatically-after-booting-the-system-and-keep-it


sudo apt-get install supervisor

sudo copy costalevigatrici.cong /etc/supervisor/conf.d  
sudo supervisorctl reread
sudo supervisorctl update

supervisorctl



https://www.atlantic.net/vps-hosting/how-to-install-and-configure-supervisor-on-ubuntu-20-04/

http://192.168.1.181:5000/



#usefull commanfs

Comandi utili
sudo supervisorctl status			per controllare l’avvio di Evo MBS
sudo supervisorctl start costalevigatrici	per avviare il servizio EVO MBS dal supervisor
sudo supervisorctl stop costalevigatrici		per fermare il servizio EVO MBS dal supervisor
cd /home/pi/costalevigatrici2
flask run –host=0.0.0.0				per avviare EVO MBS manualmente




