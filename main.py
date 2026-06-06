"""
main.py - Multi-tap Script Launcher for RP2040 Zero
  1 press  → run script1.py
  2 presses → stop current, run script2.py
  3 presses → stop current, run script3.py

Wiring:
  - One leg of the button to GPIO 28
  - Other leg to GND
  (Uses internal pull-up, no external resistor needed)
"""

import os
import time
import machine
import _thread

# ── Configuration ──────────────────────────────────────────────────────────────

BUTTON_PIN     = 28     # GPIO pin for the tactile button
DEBOUNCE_MS    = 50     # Debounce delay per press (ms)
TAP_WINDOW_MS  = 400    # Max gap between taps to count as multi-tap (ms)

# Map tap count → script filename
SCRIPT_MAP = {
    1: "effect3_bouncing_LEDs.py",
    2: "effect1_Shake_Shake.py",
    3: "effect6_Meteor.py",
    
}

# ── Setup ──────────────────────────────────────────────────────────────────────

button    = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
stop_flag = False

# ── Script runner ──────────────────────────────────────────────────────────────

def script_runner(path):
    global stop_flag
    print("[launcher] Starting: {}".format(path))
    try:
        with open(path, "r") as fh:
            src = fh.read()
        ns = {
            "__name__": "__main__",
            "__file__": path,
            "stop_flag": lambda: stop_flag,
        }
        exec(compile(src, path, "exec"), ns)
    except OSError:
        print("[launcher] File not found: {}".format(path))
    except Exception as e:
        print("[launcher] Error in {}: {}".format(path, e))
    print("[launcher] Exited: {}".format(path))


def kill_current():
    global stop_flag
    stop_flag = True
    time.sleep_ms(300)   # Give the running thread time to notice and exit


def launch(filename):
    global stop_flag
    stop_flag = False
    _thread.start_new_thread(script_runner, (filename,))

# ── Tap counter ────────────────────────────────────────────────────────────────

def count_taps():
    """
    Call this the moment a press is detected.
    Counts how many times the button is pressed within TAP_WINDOW_MS
    after the FIRST press and returns the total tap count.
    """
    taps = 1  # We already have the first press

    while True:
        deadline = time.ticks_add(time.ticks_ms(), TAP_WINDOW_MS)

        # Wait for button release first
        while button.value() == 0:
            time.sleep_ms(10)
        time.sleep_ms(DEBOUNCE_MS)

        # Now wait for another press OR timeout
        got_press = False
        while time.ticks_diff(deadline, time.ticks_ms()) > 0:
            if button.value() == 0:
                time.sleep_ms(DEBOUNCE_MS)
                if button.value() == 0:   # Confirmed press
                    taps += 1
                    got_press = True
                    break
            time.sleep_ms(10)

        if not got_press:
            break  # No more taps within the window

    # Wait for final release
    while button.value() == 0:
        time.sleep_ms(10)

    return taps

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("[launcher] Ready on GPIO {}".format(BUTTON_PIN))
    print("[launcher] 1 tap=script1  2 taps=script2  3 taps=script3")

    while True:
        # Wait for the first press
        if button.value() == 0:
            time.sleep_ms(DEBOUNCE_MS)
            if button.value() == 0:          # Confirmed
                taps = count_taps()

                if taps in SCRIPT_MAP:
                    filename = SCRIPT_MAP[taps]
                    print("[launcher] {} tap(s) → {}".format(taps, filename))
                    kill_current()
                    launch(filename)
                else:
                    print("[launcher] {} taps — not mapped, ignoring".format(taps))

        time.sleep_ms(10)


main()
