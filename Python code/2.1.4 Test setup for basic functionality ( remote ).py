# import necessary libraries and modules
import time
from Adafruit_LED_Backpack import SevenSegment
# This is library import for max7219 compatibility
from luma.led_matrix.device import max7219
# SPI communication
from luma.core.interface.serial import spi, noop
# Import canvas
from luma.core.render import canvas
import random

serial_interface = spi(port=0, device=1, gpio=noop())
# Initialise the MAX7219 device
cascaded_var = 1
block_orientation_var = 90
rotate_var = 0
max7219_device = max7219(serial_interface, cascaded=cascaded_var,
                         block_orientation=block_orientation_var,
                         rotate=rotate_var)

# initialising the bar height list for the LED matrix function
x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = -1
bar_height = [x1, x2, x3, x4, x5, x6, x7, x8]
while True:
    echo_time = random.random()
    print("Measured pulse time = ", echo_time, "S")
    echo_time = echo_time * 200

    # -------------------------------7_seg_visualization---------------------------------------------
    def seg_display(actual_distance):

        # scaling the pulse duration
        scaled_distance = echo_time / 2
        scaled_distance = str(round(scaled_distance, 1))
        print("the scaled pulse duration is", scaled_distance)
        # Define a segment object
        segment_7SD = SevenSegment.SevenSegment(address=0x70)
        # Initialise the 7SD
        segment_7SD.begin()
        segment_7SD.print_number_str(scaled_distance)  # because the maximum percentage is 100

        # Write character
        segment_7SD.write_display()


    seg_display(echo_time)
    # --------------------------------calling the function for the remote system---------------------------  
    # scalling the echo time to a value between 0 and 7
    MLD_distance = echo_time / 200 * 7
    MLD_distance = int(round(MLD_distance))
    # adding the value of the scaled echo time to the bar height list
    bar_height.append(MLD_distance)
    print(len(bar_height))
    # deleting the oldest value of bar height list
    del bar_height[0]
    print(bar_height)
    # Defining a canvas drawing environment
    with canvas(max7219_device) as draw:
        for i in range(0, 8):
            print([i, 7 - bar_height[i], i, 7 - bar_height[i]])
            draw.line([i, 7 - bar_height[i], i, 7 - bar_height[i]], fill="white")
    time.sleep(1)