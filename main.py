#
# Created by 안호성 on 2022-11-30.
#

# import
import time

import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set GPIO pinNumber
Sensor = 13
Electromagnet = 17

# GPIO Sensor and Electromagnet setup
GPIO.setup(Sensor, GPIO.IN)
GPIO.setup(Electromagnet, GPIO.OUT)

i = 1

# loop precess
while True:
    # make and set Sen var with Sensor value
    Sen = GPIO.input(Sensor)

    # Set Electromagnet On/Off with Sensor value
    if Sen:
        for i in range(3):
            time.sleep(1)
            if not Sen:
                GPIO.output(Electromagnet, GPIO.HIGH)
                pass
        print('open')
        GPIO.output(Electromagnet, GPIO.LOW)
        for i in range(10):
            time.sleep(1)
            print('open', '_',i)
    else:
        GPIO.output(Electromagnet, GPIO.HIGH)

    # running status
    print(True, i, Sen)
    i += 1

    # Delay
    time.sleep(0.05)
