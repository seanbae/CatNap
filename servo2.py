#!/usr/bin/python

from firebase import firebase
import json
import RPi.GPIO as GPIO
import time

def neutral():
    print "neutral"
    GPIO.output(11, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)

def bleed():
    print "bleed"
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    time.sleep(5)

def fill():
    print "fill"
    GPIO.output(11, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(6)#0)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

countdown = -1 # timer value in seconds
set_countdown = False
is_inflating = True
k = True
time1 = 0
time2 = 0

neutral()

firebase2 = firebase.FirebaseApplication('https://wakeuprightnowyourea.firebaseio.com', None)
while True:
    data = firebase2.get('/0', None) # {u'minutes': 0, u'force': True, u'bed': 1} 

    time2 = data['minutes']
    def is_new_data(time1, time2):
        return time2 > time1

    if is_new_data(time1, time2):
        fill()
    elif data['minutes'] <= 0:
        bleed()
    else:
        neutral()

    time1 = time2
    print data['minutes']
    print data['force']
    print data['bed']

    '''    
    if (countdown == 0 or data['force'] == True):# and k == True:
        set_countdown = False
        countdown = -1;
        bleed()
 #       k = True
    else:
       # if countdown > data['minutes'] * 60 - 90:# or k == False:
        if something:
        	fill()
#                k = False
        else :
        	neutral()

        if set_countdown == False:
         	set_countdown = True
        	countdown = data['minutes'] * 3#60
       	elif countdown > -1 :
        	countdown -= 1
    '''
    #print countdown
    #print set_countdown
    time.sleep(1)

