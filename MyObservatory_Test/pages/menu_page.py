__author__ = 'proko'

# coding:utf-8

def menu_area(driver):
    return driver.find_elements_by_xpath("//android.widget.LinearLayout")

def nine_day_forcast_btn(driver):
    return driver.find_element_by_xpath("//android.widget.LinearLayout[@index='4']")