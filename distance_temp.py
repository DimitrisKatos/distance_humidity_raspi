#!/usr/bin/env python3
#import all the libraries
import RPi.GPIO as GPIO
import time
import adafruit_dht
import board


GPIO.setmode(GPIO.BOARD)
dhtDevice= adafruit_dht.DHT11(board.D4)
GPIO_TRIGGER=12
GPIO_ECHO=18
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

def distance():
# set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance

def temp():
    temperature=dhtDevice.temperature
    return temperature

def hum():
    humidity=dhtDevice.humidity
    return humidity


if __name__=="__main__":
    try:
        while 1:
            dist=distance()
            temperature= temp()
            humidity=hum()
            print("Distance: {} cm , Temperature: {} C , Humidity: {}%".format(dist,temperature,humidity))
    except KeyboardInterrupt:
        print("programm stopped by user")
        GPIO.cleanup
    time.sleep(2)   