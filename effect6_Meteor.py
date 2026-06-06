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

# Each meteor = [position, velocity]
meteors = []

while True:

    # Spawn new meteor
    if random.random() < 0.25:
        meteors.append([0, random.randint(1, 2)])

    # Fade entire strip (trail persistence)
    for i in range(NUM_LEDS):
        r, g, b = np[i]
        np[i] = (int(r * 0.75), int(g * 0.75), int(b * 0.75))

    new_meteors = []

    for m in meteors:
        pos, speed = m

        # Draw head (bright white)
        if 0 <= pos < NUM_LEDS:
            np[pos] = scale(255, 255, 255)

        # Draw trail behind meteor
        for t in range(1, 6):
            p = pos - t
            if 0 <= p < NUM_LEDS:
                fade = 255 - (t * 40)
                np[p] = scale(fade, fade // 2, 0)

        # Move meteor forward
        pos += speed

        if pos < NUM_LEDS + 6:
            new_meteors.append([pos, speed])

    meteors = new_meteors

    np.write()
    time.sleep_ms(50)