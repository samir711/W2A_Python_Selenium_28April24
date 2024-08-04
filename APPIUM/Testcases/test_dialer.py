import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By


def test_dialer_app():
    desired_capabilities = {

        "platformName": "Android",
        "appium:deviceName": "Pixel 8 Pro API 34",
        "appium:appPackage": "com.google.android.dialer",
        "appium:appActivity": "com.google.android.dialer.extensions.GoogleDialtactsActivity",
        "appium:automationName": "UIAutomator2"
    }
    appium_server_url = "http://127.0.0.1:4723"
    cap_options = UiAutomator2Options().load_capabilities(desired_capabilities)
    driver = webdriver.Remote(appium_server_url, options=cap_options)
    print(driver.session_id)
    driver.find_element(By.ID,"com.google.android.dialer:id/dialpad_fab").click()
    driver.find_element(By.ID,"com.google.android.dialer:id/four").click()
    driver.find_element(By.ID,"com.google.android.dialer:id/three").click()
    driver.find_element(By.ID,"com.google.android.dialer:id/seven").click()
    driver.find_element(By.ID,"com.google.android.dialer:id/three").click()
    driver.find_element(By.ID,"com.google.android.dialer:id/four").click()
    driver.find_element(By.ID,"com.google.android.dialer:id/four").click()
    driver.find_element(By.ID,"com.google.android.dialer:id/one").click()
    driver.find_element(By.ID,"com.google.android.dialer:id/one").click()
    driver.find_element(By.ID,"com.google.android.dialer:id/zero").click()
    driver.find_element(By.ID,"com.google.android.dialer:id/eight").click()
    driver.find_element(By.ID,"com.google.android.dialer:id/dialpad_voice_call_button").click()
    time.sleep(6)
    driver.find_element(By.ID,"com.google.android.dialer:id/incall_end_call").click()
    time.sleep(6)
    driver.quit()
