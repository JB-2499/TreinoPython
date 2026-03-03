import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.hotkey('ctrl', 'h')
pyautogui.press('f11')

time.sleep(2)

for i in range(5):
    pyautogui.press('tab')

pyautogui.press('enter')
pyautogui.press('f11')