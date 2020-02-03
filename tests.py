import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

path = os.path.abspath(os.path.dirname(__file__))
file_p = os.path.join(path, 'file.txt')

try:

    browser.implicitly_wait(5)

    button_element = browser.find_element(By.CSS_SELECTOR, "#book")
    WebDriverWait(browser, timeout=10).until(
        expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#price'), "100"
        )
    )
    button_element.click()

    windows = browser.window_handles
    print(len(windows))
    browser.switch_to.window(windows[-1])

    x_el = browser.find_element_by_id('input_value')
    x = int(x_el.text)
    y = calc(x)

    input_el = browser.find_element_by_id('answer')
    input_el.send_keys(y)

    button_element = browser.find_element(By.CSS_SELECTOR, '#solve')
    button_element.click()


finally:
    time.sleep(5)
    browser.quit()
