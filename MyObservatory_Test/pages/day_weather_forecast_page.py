__author__ = 'proko'


# coding:utf-8

def day(driver):
    return driver.find_element_by_id('hko.MyObservatory_v1_0:id/sevenday_forecast_day_of_week')


def day_area(driver):
    return driver.find_elements_by_xpath("//android.widget.LinearLayout")
