import machine
import time

# Define all the pins on the board
pins = [machine.Pin(i, machine.Pin.OUT) for i in range(28)]

while True:
    # Turn on all the pins
    print("Pins On")
    for pin in pins:
        pin.value(1)
    time.sleep(3)

    # Turn off all the pins
    print("Pins Off")
    for pin in pins:
        pin.value(0)
    time.sleep(3)
