# -*- coding: utf-8 -*-


from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
import time
import os
import sys
from signal import pause
import Adafruit_DHT as dht

app = Flask(__name__,template_folder='templates')
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#read data using pin17
h,t = dht.read_retry(dht.DHT22,17)
Temp='{0:0.1f}*C'.format(t)
time.sleep(1)
print "DOne"
a=1
@app.route("/")
def index():
	return render_template('index.html',Temp=Temp)	
	# Read Temperature pin 17
	#h,t = dht.read_retry(dht.DHT22,17)
	#Temp=('{0:0.1f}*C'.format(t))
	#if t is not None:
		#print('Temp={0:0.1f}*C  Humidity={1:0.1f}%' .format(t, h))
    		#return render_template('index.html')
		#Temp='{0:0.1f}*C'.format(t)
    
if __name__ == "__main__":
	print "Start"
	debug = True
	app.run(host='192.168.0.102',port=2222)
