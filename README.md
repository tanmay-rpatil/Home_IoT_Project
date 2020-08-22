# Home_iot_project
MQTT based IoT project with a web dashboard.

## Screenshot 
![alt text](https://github.com/tanmay-rpatil/Home_IoT_Project/ScreenShots/ss1.png "Dashboard Screenshot")

## Intro
* The backend is written in python, using the Django framework. 
* The front-end uses CSS and from Material Dashboard (Linked below), with ajax calls added by me.
* The IoT devie is a NodeMCU esp8266, with a DHT11 (3 pin) temperature and humidity sensor.
* The device sends data via the MQTT protocol, to a local MQTT broker.
* A python script runs in the backdround, subscribes to the MQTT topic and regularly updates the database.




## NOTE
CSS and JS credit to [Material Dashboard by Creative Tim](https://github.com/creativetimofficial/material-dashboard)
