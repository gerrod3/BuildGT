import RPi.GPIO as GPIO
import time

def stop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(15,GPIO.LOW)

def start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(15,GPIO.HIGH)
