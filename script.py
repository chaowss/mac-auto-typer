import os
import sys
import time
from pynput import keyboard
import pyautogui

# Check for admin privileges on macOS
if os.name == "posix" and not os.geteuid() == 0:
    print("This script must be run as root on macOS. Try running with `sudo`.")
    sys.exit(1)

# List of strings to type
strings = [
    "Hello, this is the first string.",
    "Here's the second string for you.",
    "Finally, the last string to type."
]

# Disable pyautogui's failsafe and set no delay
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

# State variables
current_index = 0
typing = False

def type_string():
    """Simulates typing the current string."""
    global typing, current_index
    if typing or current_index >= len(strings):
        return
    typing = True
    pyautogui.write(strings[current_index], interval=0.0001)  # Much faster typing
    typing = False
    current_index += 1

def on_press(key):
    if key == keyboard.Key.esc:
        # Stop listener and exit program
        os._exit(0)
    elif key == keyboard.Key.ctrl:
        type_string()

# Create and start the listener
print("Press 'Control' to type the next string")
print("Press 'Escape' to exit")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()