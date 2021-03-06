#!/usr/bin/env python3
"""
The goal of this example is to show you the syntax for IR seeking readings.  When using
IR-SEEK with a remote control you get both heading and distance data.  The code below
shows the syntax for beacon seeking.  Additionally it's good to play with a demo so that
you can see how well or not well a sensor behaves.

To test this module, put the IR Remote into beacon mode by pressing the button at the top
of the remote and making sure the green LED is on.  Use channel 1 for this module.  Move
the beacon around and watch the values that are printed.

Authors: David Fisher and PUT_YOUR_NAME_HERE.
"""

import ev3dev.ev3 as ev3
import time


def main():
    print("--------------------------------------------")
    print(" Printing beacon seeking data")
    print(" Press the touch sensor to exit")
    print("--------------------------------------------")
    ev3.Sound.speak("Printing beacon seeking").wait()

    touch_sensor = ev3.TouchSensor()
    beacon_seeker = ev3.BeaconSeeker()
    assert touch_sensor
    assert beacon_seeker

    while not touch_sensor.is_pressed:
        current_heading = beacon_seeker.heading
        current_distance = beacon_seeker.distance
        print("IR Heading = {}   Distance = {}".format(current_heading, current_distance))
        time.sleep(0.5)

    ev3.Sound.speak("Goodbye")


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
