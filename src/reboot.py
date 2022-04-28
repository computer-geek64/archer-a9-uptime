#!/usr/local/bin/python3 -B
# reboot.py

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def reboot():
    options = webdriver.FirefoxOptions()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.get('http://192.168.0.1/webpages/login.html')

    sleep(20)

    password_input = driver.find_elements(By.CSS_SELECTOR, 'input.l[type=password]')[2]
    password_input.send_keys(os.environ['ROUTER_PASSWORD'])
    password_input.send_keys(Keys.ENTER)

    sleep(20)

    driver.find_element(By.CSS_SELECTOR, 'a#top-control-reboot').click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#reboot_confirm_msg button.btn-msg-ok').click()

    driver.close()


if __name__ == '__main__':
    reboot()
