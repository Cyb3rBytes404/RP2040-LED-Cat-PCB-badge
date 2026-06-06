import machine, neopixel, time

# Setup
pin = machine.Pin(9, machine.Pin.OUT)
n = 30
np = neopixel.NeoPixel(pin, n)

# Brightness (0.0 to 1.0)
brightness = 0.2

# Base colors
base_colors = [
    (255, 0, 0),   # Red
    (0, 0, 255),   # Blue
    (0, 255, 0)    # Green
]

# Apply brightness to color
def apply_brightness(color, brightness):
    return (
        int(color[0] * brightness),
        int(color[1] * brightness),
        int(color[2] * brightness)
    )

# Clear all LEDs
def clear():
    np.fill((0, 0, 0))
    np.write()

while True:

    # Loop through each color
    for base_color in base_colors:

        color = apply_brightness(base_color, brightness)

        # Forward direction
        for i in range(n):
            np.fill((0, 0, 0))
            np[i] = color
            np.write()
            time.sleep(0.05)

        # Reverse direction
        for i in range(n - 2, -1, -1):
            np.fill((0, 0, 0))
            np[i] = color
            np.write()
            time.sleep(0.05)