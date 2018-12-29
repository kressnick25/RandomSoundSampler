import os, random
from time import sleep
import sys

#Modify these to correct path to files
path = '/path/to/folder'
#sound to play inside path on startup
startupSound = 'file'

#Check if script running on a Raspberry Pi
currentOS = os.uname()[4][:3]

if currentOS == 'arm':
        import RPi.GPIO as GPIO

# When using a RasPi, use GPIO button as wait input
def setup_GPIO():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setwarnings(False)

def run_keyboard():
        os.system('mpg123 ' + path + startupSound)
        while True:
                input()
                os.system('killall mpg123')
                rand_file = random.choice(os.listdir(path))
                os.system('mpg123 ' + path + rand_file)
                sleep(0.25)     

def run_GPIO():
        os.system('mpg123 ' + path + startupSound + ' >/dev/null 2>&1 &')
        while True:
                if GPIO.input(10) == GPIO.HIGH:
                        os.system('killall mpg123')
                        rand_file = random.choice(os.listdir(path + "$"))
                        os.system('mpg123 ' + path + rand_file + ' >/d$')
                sleep(0.25)

# Running on RasPi
if currentOS == 'arm':
        setup_GPIO()
        run_GPIO()

# Windows, MacOs or Linux
else:
        run_keyboard()
