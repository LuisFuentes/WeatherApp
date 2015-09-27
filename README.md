Weather App
==============================================
This is a simple weather app that provides a RESTful API to display a
customizable weather ticket.

Developing with the Weather App
------------------------
First, install pip.
```bash
sudo apt-get install python-pip
```
Next, install the virtual environment - virtualenv.
```bash
pip install virtualenv
```
Now setup the pyelixys sandbox environment
```bash
virtualenv WeatherApp
cd WeatherApp
```
Active the sandbox environment
```bash
source bin/activate
```
Clone the repository
```bash
git clone git@github.com:luisfuentes/WeatherApp.git
cd WeatherApp
```
Install the python dependencies using pip
```bash
pip install -r requirements.txt
```

Starting the Weather App Web Service
------------------------------------------
To run the Weather App web service, activate the virtual
environment and execute the command:
```bash
. ~/bin/activate
python ~/WeatherApp/runserver.py
```
