# RP2040-LED-Cat-PCB-badge
Cyb3rBytes: The Ultimate Mini-DefCon badge for Future Tech Heroes!

Welcome to the official repository for the ** Cyb3rBytes ** cyber coding camp! 

This repository contains all the MicroPython starter scripts, libraries, and code challenges you need to light up your custom RP2040 cyber badge. Team up with our cyber-cat mascot, grab your badge, and let's start hacking/coding (the ethical way)!

---

## 🛠️ What's Inside Your Badge?
*   **The Brain:** Raspberry Pi RP2040 Microcontroller and a MPU-6050 Module 3 Axis Gyroscope Accelerometer Module
*   **The Lights:** 30x WS2812 RGB LEDs (NeoPixels!)
*   **The Language:** MicroPython 🐍

---

## 🚀 Step 1: Clone the Code
Open your terminal or command prompt and type this command to download all the project files to your computer:

```bash
git clone https://github.com
```

*(If you don't have Git, just click the green **Code** button at the top of this page and select **Download ZIP**!)*

---

## 🔌 Step 2: Connect Your Badge
1. Grab your USB-C cable.
2. Plug one end into your computer and the other into your cyber-cat badge.
3. Open **Thonny IDE** (or your camp's preferred code editor).
4. Look at the bottom right corner of Thonny and make sure it says: **MicroPython (Raspberry Pi Pico)**.

⚠️ **Cat Safety Rule:** Always hold your PCB badge by the edges! Try not to touch the shiny metal pins while it is plugged in. and absolutely no water, real cats don’t like water neither does this one.. 

---

## 💾 Step 3: Install the Light Library
Before we can make the lights flash, your badge needs to know how to talk to WS2812 LEDs. 

1. In this repository, find the file named `neopixel.py`.
2. Open it in Thonny.
3. Click **File > Save As**, choose **MicroPython Device**, and save it exactly as `neopixel.py`.

---

## 🐍 Step 4: Your First Code Challenge (Test the Lights!)
Open a new file in Thonny, copy the code below, and click the green **Run** button to turn the first LED bright green!

```python
import machine
import neopixel
import time

# Setup the 30 LEDs on Pin 16 (Check your badge pin number!)
NUM_LEDS = 30
DATA_PIN = 9
badge = neopixel.NeoPixel(machine.Pin(DATA_PIN), NUM_LEDS)

# Cyb3rSpark619 Boot Sequence
print("Cyber-Cat Badge Initialized!")

# Turn on the very first LED (0 is the first one in coding!)
# Colors are (Red, Green, Blue) from 0 to 255
badge[0] = (0, 255, 0) 
badge.write()

print("🟢 Success! First light is active.")
```

---

## 🏆 Cyber Challenges to Unlock
Check the `challenges/` folder in this repo to find code templates for:
*   [ ] **Challenge 1:** Light up all 30 LEDs at once.
*   [ ] **Challenge 2:** Make the badge blink like a police siren (Red and Blue).
*   [ ] **Challenge 3:** Create a moving "Knight Rider" laser scan effect.
*   [ ] **Challenge 4 (Mega Boss):** Code a smooth, rainbow cycle animation!

---

## 🛡️ Ethical Hacker Oath
> *"I promise to use my coding superpowers for good, to protect digital spaces, to fix glitches, and to help others stay safe online!"*

Have fun coding your badge, and welcome to the regional **Cyb3rSpark619** team! 🐾
