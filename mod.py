import time
import selenium
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
from undetected_chromedriver import ChromeOptions
import os 


#Driver online
def driver(raw_path):
    opts = uc.ChromeOptions()
    opts.add_argument("--mute-audio")
    script_directory = os.path.dirname(os.path.abspath(__file__))
    chrome_binary_path = os.path.join(script_directory, "chrome-win", "chrome.exe")
    chrome_driver_path = os.path.join(script_directory, "chromedriver.exe")
    browser = uc.Chrome(browser_executable_path=chrome_binary_path, executable_path=chrome_driver_path,
                        user_data_dir=raw_path,
                        mute=True, options=opts)
    return browser







def hidden_driver(raw_path):
    opts = uc.ChromeOptions()
    opts.add_argument("--mute-audio")
    script_directory = os.path.dirname(os.path.abspath(__file__)) 
    chrome_binary_path = os.path.join(script_directory, "chrome-win", "chrome.exe")
    chrome_driver_path = os.path.join(script_directory, "chromedriver.exe")
    browser = uc.Chrome(browser_executable_path=chrome_binary_path, executable_path=chrome_driver_path,
                        user_data_dir=raw_path,
                        headless=True, use_subprocess=False, mute_audio=True, options=opts)
    return browser