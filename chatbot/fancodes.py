import time
import sys
import re
import RPi.GPIO as GPIO
from dotenv import dotenv_values

# 16 bits identifier, 9 bits command code
commands = { 'off': '111111101',    # Fan off
             '1'  : '111111111',    # Fan 1
             '2'  : '111010101',    # Fan 2
             '3'  : '111100101',    # Fan 3
             '4'  : '111101101',    # Fan 4
             '5'  : '111101011',    # Fan 5
             'lx' : '010000111',    # Light
             'rev': '111100011' }   # Fan reverse

# Read fan IDs from .env file
fan_ids = dotenv_values()
# Remove all env values which are not binary strings
for key in list(fan_ids.keys()):
    if not re.match('[0|1]{16}', fan_ids[key]):
        del fan_ids[key]

short_delay = 0.00025
long_delay = 0.00050
extended_delay = 0.0099

NUM_ATTEMPTS = 5
TRANSMIT_PIN = 17

# Transmit given command string to all fans
def transmit_all(command):
    for fan_code in fan_ids.values():
        transmit_code(fan_code + commands[command])
        time.sleep(0.4)

# Take fan_id and command, translate to code and transmit
def transmit_command(fan_id, command, count = 1):
    code = fan_ids[fan_id] + commands[command]
    for _ in range(count):
        transmit_code(code)
        time.sleep(1)

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    print(code)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        for i in code:
            if i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(short_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_delay)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(long_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(extended_delay)
    GPIO.cleanup()
