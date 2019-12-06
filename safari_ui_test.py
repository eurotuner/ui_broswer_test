#! /usr/local/bin/python3

import time
import pyautogui
from selenium import webdriver

def website(URL):
   browser = webdriver.Safari(executable_path = "/usr/bin/safaridriver")
   browser.get(URL)
   search_bar = browser.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input") # Finds search bar
   search_bar.click()
   pyautogui.typewrite("github", interval = 0.5); pyautogui.hotkey("return")  # Enters search results
   time.sleep(3)
   pyautogui.moveTo(464, 316, duration = 1.2); pyautogui.click()   # Clicks on a item
   time.sleep(3)
   pyautogui.hotkey("command", "d"); pyautogui.hotkey("return")    # Creates a bookmark
   time.sleep(5)
   browser.back()
   time.sleep(3)
   pyautogui.hotkey("command", "q")   # Quits browser


cycle = 0

while cycle < 1:
   website("https://google.com")
   cycle+=1
