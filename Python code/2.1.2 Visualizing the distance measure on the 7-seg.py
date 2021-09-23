# import necessary libraries and modules
import RPi.GPIO as GPIO
import time
from Adafruit_LED_Backpack import SevenSegment

while 1:
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
    # -----------------------Defining the ultrasonic function-----------------------
    
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


    # calling the ultrasonic function

    echo_time = ultrasonic_function(PinTrigger, PinEcho)
    # printing the measured_pulse_time value
    print("Measured pulse time = ", echo_time, "S")

    # -------------------------------7_seg_visualization---------------------------------------------

    def seg_display(actual_distance):

        # scaling the echo time
        scaled_distance = echo_time * 100 / 200 * 17241
        scaled_distance = str(round(scaled_distance, 1))
        print("the scaled pulse duration is", scaled_distance)
        # Define a segment object
        segment_7SD = SevenSegment.SevenSegment(address=0x70)
        # Initialise the 7SD
        segment_7SD.begin()
        segment_7SD.print_number_str(scaled_distance)

        # Write character
        segment_7SD.write_display()


    # --------------------------------calling the 7-segement function for the normal system---------------------------
    seg_display(echo_time)
    time.sleep(1)
