from machine import Pin
import neopixel
import time
import random

NUM_LEDS = 30
DATA_PIN = 9
BRIGHTNESS = 0.15

np = neopixel.NeoPixel(Pin(DATA_PIN), NUM_LEDS)

def scale(r, g, b):
    return (
        int(r * BRIGHTNESS),
        int(g * BRIGHTNESS),
        int(b * BRIGHTNESS)
    )

# Brightness values for the trail
trail = [0] * NUM_LEDS

while True:

    # Fade existing trail
    for i in range(NUM_LEDS):
        trail[i] = max(0, trail[i] - 25)

    # Randomly create new rain drops
    if random.random() < 0.4:
        trail[random.randint(0, NUM_LEDS - 1)] = 255

    # Draw strip
    for i in range(NUM_LEDS):

        brightness = trail[i]

        if brightness > 220:
            # White-hot leading character
            np[i] = scale(
                brightness,
                brightness,
                brightness
            )
        else:
            # Matrix green trail
            np[i] = scale(
                0,
                brightness,
                0
            )

    np.write()
    time.sleep_ms(50)