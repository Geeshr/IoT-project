import machine
import utime

# Initialize the LED pin
led = machine.Pin(7, machine.Pin.OUT)

try:
    while True:
        led.value(1)      # Turn the LED on
        utime.sleep(2)    # Wait for 2 seconds
        led.value(0)      # Turn the LED off
        utime.sleep(2)    # Wait for 2 seconds
except KeyboardInterrupt:
    pass
finally:
    led.value(0)  # Turn off the LED
