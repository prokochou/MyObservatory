__author__ = 'proko'


# coding:utf-8

def AgreeBtn(driver):
    return driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)')


def MenuBtn(driver):
    return driver.find_element_by_accessibility_id("Navigate up")
