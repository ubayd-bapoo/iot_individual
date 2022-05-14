# IOT Individual Project
## Overview
Running MQTT client and Websocket client to connect to a Django server for processing.

## Installation
### Initial Installation
Install Python 3.7

Once Python is installed. Install virtualenv via pip so that all 
dependencies are stored inside the virtual environment.

```bash
pip install virtualenv
```

Create virtual environment using the following command:
```bash
virtualenv venv
```

Activate the virtual environment. On Windows use the following.
```bash
venv\Scripts\activate.bat
```

If any packages are unable to install. Go to the following link and
install them manually, Windows only. [Python .whl files](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

## Setup
Run the django migrate
```bash
python manage.py migrate
``` 

## Commands for Broker
Run MQTT broker:
net start mosquitto

Stop Broker:
net stop mosquitto

## Commands to run Clients
Navigate to the root of the repo
```bash
sudo venv/bin/python client/websocket_client.py
``` 
```bash
sudo venv/bin/python client/mqtt_client.py
``` 

