# import pyautogui
# import time
#
# pyautogui.hotkey("win", "r")
# pyautogui.typewrite("chrome")
# pyautogui.press("enter")
# time.sleep(0.5)
# # typewrite("https://ege.fipi.ru/bank/index.php?proj=B9ACA5BBB2E19E434CD6BEC25284C67F")
# pyautogui.typewrite("https://ege.fipi.ru/bank/index.php?proj=B9ACA5BBB2E19E434CD6BEC25284C67F")
# pyautogui.press('enter')
# time.sleep(5)
# screen = pyautogui.screenshot("screenshot123.png")
# print(screen)

from selenium import webdriver

driver = webdriver.Chrome(executable_path='"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
driver.get("https://ege.fipi.ru/bank/index.php?proj=B9ACA5BBB2E19E434CD6BEC25284C67F")

in1 = driver.find_element_by_name('answer')
in1.send_keys('моя_супер_учетная_запись')
