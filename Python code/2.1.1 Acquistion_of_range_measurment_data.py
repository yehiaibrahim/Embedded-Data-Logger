# import necessary libraries and modules
import RPi.GPIO as GPIO
import time

# Define GPIO numbering mode
GPIO.setmode(GPIO.BCM)
# Define pins of Trigger and Echo pin
PinTrigger = 16
PinEcho = 12
# Define Trigger pin as output
GPIO.setup(PinTrigger, GPIO.OUT)
# Define Echo pin as input
GPIO.setup(PinEcho, GPIO.IN)
# Set Trigger pin to false and wait for 1 sec.
print('Initialising Sensor')
GPIO.output(PinTrigger, False)
time.sleep(1)


def ultrasonic_function(trigger_pin, echo_pin):
    # Set Trigger for 1ms to TRUE and reset afterwards
    print('Sending Trigger signal')
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)
    # Measure t1 as long as echo pin is FALSE
    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()
    # Measure t2 as long as echo pin is TRUE
    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()
    # Calculate pulse duration
    pulse_duration = pulse_end - pulse_start
    # Returning the pulse duration
    return pulse_duration


# ----------------------------- calling the ultrasonic function -------------------------------------


echo_time = ultrasonic_function(PinTrigger, PinEcho)
# printing the measured pulse time value
print("Measured pulse time = ", echo_time, "S")
