#! /usr/local/bin/python3

import time
import pyautogui
from selenium import webdriver

def website(URL):
    browser = webdriver.Firefox()
    browser.get(URL)
    search_bar = browser.find_element_by_css_selector(".gLFyf") # Finds search bar
    search_bar.click()
    pyautogui.typewrite("github", interval = 0.5); pyautogui.hotkey("return")  # Enters search results
    time.sleep(3)
    pyautogui.moveTo(464, 316, duration = 1.2); pyautogui.click()   # Clicks on a item
    time.sleep(3)
    pyautogui.hotkey("ctrl", "d"); pyautogui.hotkey("return")    # Creates a bookmark
    time.sleep(5)
    browser.back()
    time.sleep(3)
    pyautogui.hotkey("ctrl", "q")   # Quits browser


cycle = 0

while cycle < 1:
    website("https://google.com")
    cycle+=1
