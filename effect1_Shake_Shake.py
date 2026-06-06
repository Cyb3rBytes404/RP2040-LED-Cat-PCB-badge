from machine import Pin, I2C
import neopixel
import struct
import time
import math

# -------------------------
# Hardware Setup
# -------------------------

LED_PIN = 9
NUM_LEDS = 30

np = neopixel.NeoPixel(Pin(LED_PIN), NUM_LEDS)

ADDR = 0x18

i2c = I2C(0, scl=Pin(5), sda=Pin(4))

# LIS3DH: 100Hz, XYZ enabled
i2c.writeto_mem(ADDR, 0x20, b'\x57')

# -------------------------
# Accelerometer
# -------------------------

def read_accel():
    data = i2c.readfrom_mem(ADDR, 0x28 | 0x80, 6)

    x = struct.unpack('<h', data[0:2])[0] >> 4
    y = struct.unpack('<h', data[2:4])[0] >> 4
    z = struct.unpack('<h', data[4:6])[0] >> 4

    return x, y, z

# -------------------------
# Pulse Storage
# -------------------------

pulses = []

last_mag = 0

# -------------------------
# Main Loop
# -------------------------

while True:

    # Read acceleration
    x, y, z = read_accel()

    mag = math.sqrt(x*x + y*y + z*z)

    delta = abs(mag - last_mag)
    last_mag = mag

    # Detect shake
    if delta > 80:

        brightness = min(int(delta * 2), 255)

        # Choose color based on strength
        if delta < 150:
            color = (0, 0, brightness)          # Blue
        elif delta < 300:
            color = (0, brightness, 0)          # Green
        elif delta < 500:
            color = (brightness, brightness, 0) # Yellow
        else:
            color = (brightness, 0, 0)          # Red

        pulses.append({
            "pos": 0.0,
            "speed": 0.6,
            "color": color
        })

        print("Shake:", int(delta))

    # Clear strip
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)

    # Draw pulses
    active = []

    for pulse in pulses:

        pos = pulse["pos"]
        color = pulse["color"]

        # Head
        idx = int(pos)

        if 0 <= idx < NUM_LEDS:
            np[idx] = color

        # Trail
        for trail in range(1, 6):

            trail_idx = idx - trail

            if 0 <= trail_idx < NUM_LEDS:

                fade = 1.0 - (trail / 6.0)

                np[trail_idx] = (
                    int(color[0] * fade),
                    int(color[1] * fade),
                    int(color[2] * fade)
                )

        pulse["pos"] += pulse["speed"]

        if pulse["pos"] < NUM_LEDS + 5:
            active.append(pulse)

    pulses = active

    np.write()

    time.sleep(0.02)