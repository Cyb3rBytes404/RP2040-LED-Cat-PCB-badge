import machine, neopixel, time, random

# Setup
pin = machine.Pin(9, machine.Pin.OUT)
n = 30
np = neopixel.NeoPixel(pin, n)

# Brightness (0.0 to 1.0)
brightness = 0.2

# Number of twinkling stars
star_count = 6

# Star color (soft white)
base_color = (255, 255, 255)

# Apply brightness
def apply_brightness(color, brightness):
    return (
        int(color[0] * brightness),
        int(color[1] * brightness),
        int(color[2] * brightness)
    )

# Clear LEDs
def clear():
    np.fill((0, 0, 0))
    np.write()

clear()

while True:

    # Slight fade of all LEDs
    for i in range(n):

        r, g, b = np[i]

        # Fade each color channel
        r = max(0, r - 10)
        g = max(0, g - 10)
        b = max(0, b - 10)

        np[i] = (r, g, b)

    # Randomly create new stars
    for _ in range(star_count):

        pixel = random.randint(0, n - 1)

        color = apply_brightness(base_color, brightness)

        np[pixel] = color

    np.write()

    time.sleep(0.05)