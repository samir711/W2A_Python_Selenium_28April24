from selenium import webdriver

browser = webdriver.Firefox()

def load(URL):
    browser.get(URL)
    browser.maximize_window()
    return browser

def stop():
    browser.quit()