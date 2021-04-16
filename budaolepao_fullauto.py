#必须用管理员权限运行
import pyautogui
import time

time.sleep(5)
pyautogui.moveTo(822, 105, duration = 3)
while True:
    pyautogui.click()
    pyautogui.moveRel(121, 0, duration = 1)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveRel(-121, 0, duration = 1)