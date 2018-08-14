#!/usr/bin/env python3

import pygame.midi as midi
import time, sys

# Global vars
namePattern = "Launchpad MK2"

# Initialize midi
midi.init()

deviceCount = midi.get_count()
print( f"Number of MIDI-devices: {deviceCount}" )

# List all devices and locate launchpad
inputDeviceIndex  = None
outputDeviceIndex = None
for i in range(deviceCount):
    (interface, name, isinput, isoutput, opened ) = midi.get_device_info( i )
    print()
    direction = "UNKNOWN"
    if ( isinput ):
        direction = "INPUT"
    elif ( isoutput ):
        direction = "OUTPUT"
    print( f"    [{direction}{', opened' if opened else ''}]" )
    print( f"    Device:    {i}" )
    print( f"    Interface: {interface.decode()}" )
    print( f"    Name:      {name.decode()}" )

    # Check if device we're looking for
    if ( name.decode().find( namePattern ) ):
        if ( isoutput ):
            outputDeviceIndex = i
        elif ( isinput ):
            inputDeviceIndex = i


# Open launchpad device(s)
outputDevice = midi.Output( outputDeviceIndex )


# Play with colors

# Clear LED:s
for i in range( 9 ):
    for j in range( 9 ):
        # Turn off all lights
        outputDevice.write_short( 0x80, (i * 10) + j )

# Cycle all colours on center pads
for i in range( 128 ):
    outputDevice.write_short(0x90,54,i)
    outputDevice.write_short(0x90,55,i)
    outputDevice.write_short(0x90,44,i)
    outputDevice.write_short(0x90,45,i)
    time.sleep( 0.05 )

# Clear LED:s
for i in range( 9 ):
    for j in range( 9 ):
        # Turn off all lights
        outputDevice.write_short( 0x80, (i * 10) + j )

# Flash LED:s red and blue
outputDevice.write_short(0x90,54,5) # red
outputDevice.write_short(0x90,55,5) # red
outputDevice.write_short(0x90,44,5) # red
outputDevice.write_short(0x90,45,5) # red
outputDevice.write_short(0x91,54,45) # blue
outputDevice.write_short(0x91,55,45) # blue
outputDevice.write_short(0x91,44,45) # blue
outputDevice.write_short(0x91,45,45) # blue

time.sleep( 5 )

# Clear LED:s
for i in range( 9 ):
    for j in range( 9 ):
        # Turn off all lights
        outputDevice.write_short( 0x80, (i * 10) + j )

# Pulse center leds
outputDevice.write_short(0x92,54,53)
outputDevice.write_short(0x92,55,53)
outputDevice.write_short(0x92,44,53)
outputDevice.write_short(0x92,45,53)

time.sleep( 5 )

# Clear LED:s
for i in range( 9 ):
    for j in range( 9 ):
        # Turn off all lights
        outputDevice.write_short( 0x80, (i * 10) + j )

# Close device
outputDevice.close()

# Quit the midi module
midi.quit()