import pyautogui
import time

def auto_click(interval, clicks, x, y):
    click_counter = 0
    for _ in range(clicks):
        pyautogui.moveTo(x, y)
        pyautogui.click()
        click_counter += 1
        if click_counter % 500 == 0:
            print(f"{click_counter} clicks completed.")
        time.sleep(interval)

# Set the interval between clicks in seconds
interval = 0.1

# Set the number of clicks
clicks = 15000

# Set the coordinates (x, y) where you want to click
x = 500
y = 500

# Run the auto-clicker
auto_click(interval, clicks, x, y)
