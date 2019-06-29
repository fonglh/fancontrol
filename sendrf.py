import time
import sys
import RPi.GPIO as GPIO

# Pass these variable names as arguments to test.
# Replace the codes with those transcribed from output of plot.py
rm_on = '1111111111111111000000000'
rm_off = '1111111111111111000000001'
rm_light = '1111111111111111000000010'

# Replace these values with those measured from output of plot.py
short_delay = 0.00025
long_delay = 0.00050
extended_delay = 0.0099

NUM_ATTEMPTS = 7
TRANSMIT_PIN = 17

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    print code
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

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')
