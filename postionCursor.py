import pyautogui
import time
# Get the current position of the mouse cursor
while True:
    x, y = pyautogui.position()

    # Print the current position
    print(f"Current position: ({x}, {y})")
    time.sleep(1)