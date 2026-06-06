from machine import Pin
import neopixel
import time
import random

NUM_LEDS = 30
BRIGHTNESS = 0.1  # 10%

np = neopixel.NeoPixel(Pin(9), NUM_LEDS)

while True:
    np.fill((0, 0, 0))

    for _ in range(5):
        p = random.randint(0, NUM_LEDS - 1)

        np[p] = (
            int(255 * BRIGHTNESS),
            int(255 * BRIGHTNESS),
            int(255 * BRIGHTNESS)
        )

    np.write()
    time.sleep_ms(100)