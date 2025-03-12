import pyautogui as pg
import time

for i in range(10):
    pg.screenshot(f"print{i}.png")
    time.sleep(2)
