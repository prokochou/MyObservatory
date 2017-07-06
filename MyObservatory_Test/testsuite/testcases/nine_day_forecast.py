__author__ = 'proko'

# coding:utf-8

import os
import unittest
from appium import webdriver
from time import sleep, gmtime, strftime
import json
import sys

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
)

sys.path.insert(0, PATH('../../'))

with open(PATH('../../config_collection/device_settings.json'), 'r') as f:
    data = json.load(f)
from pages import main_page, menu_page, day_weather_forecast_page


class NineDayForecast(unittest.TestCase):
    def setUp(self):
        desired_caps = data['capabilities']
        desired_caps['app'] = PATH(desired_caps['app'])
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def get_date(self):
        week_dic = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}
        week_number_dic = {1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat', 7: 'Sun'}
        today = strftime("%a", gmtime())
        today_value = week_dic[today]

        # generate the correct answer list
        cor_anw_ls = []
        for i in range(1, 9):
            day_value = today_value + i
            if day_value > 7:
                day_value_check = day_value - 7
                anw_day = week_number_dic[day_value_check]
                cor_anw_ls.append(anw_day)
            else:
                anw_day = week_number_dic[day_value]
                cor_anw_ls.append(anw_day)

        return cor_anw_ls

    def scroll_forecast(self):
        # Because the resource-id is the same and no content-desc value,
        # need to use scroll to check each days.

        self.driver.implicitly_wait(2)
        self.driver.drag_and_drop(day_weather_forecast_page.day_area(self.driver)[0],
                                  day_weather_forecast_page.day_area(self.driver)[5])
        self.driver.drag_and_drop(day_weather_forecast_page.day_area(self.driver)[0],
                                  day_weather_forecast_page.day_area(self.driver)[5])
        self.driver.drag_and_drop(day_weather_forecast_page.day_area(self.driver)[0],
                                  day_weather_forecast_page.day_area(self.driver)[5])

        self.driver.drag_and_drop(day_weather_forecast_page.day_area(self.driver)[0],
                                  day_weather_forecast_page.day_area(self.driver)[5])
        self.driver.drag_and_drop(day_weather_forecast_page.day_area(self.driver)[0],
                                  day_weather_forecast_page.day_area(self.driver)[5])
        self.driver.drag_and_drop(day_weather_forecast_page.day_area(self.driver)[0],
                                  day_weather_forecast_page.day_area(self.driver)[5])
        self.driver.drag_and_drop(day_weather_forecast_page.day_area(self.driver)[0],
                                  day_weather_forecast_page.day_area(self.driver)[5])

        self.driver.drag_and_drop(day_weather_forecast_page.day_area(self.driver)[0],
                                  day_weather_forecast_page.day_area(self.driver)[5])

        sleep(3)

    def test_nine_day_forecast(self):
        # Click the agree button on no responsibility announcement
        main_page.AgreeBtn(self.driver).click()
        sleep(2)

        # Click the agree button on privacy announcement
        main_page.AgreeBtn(self.driver).click()
        sleep(2)

        # Allow location permission
        main_page.AgreeBtn(self.driver).click()

        # Close Version Update Details
        main_page.AgreeBtn(self.driver).click()

        # pause a moment, so xml generation can occur
        self.driver.implicitly_wait(2)

        # Open Side Menu
        self.driver.implicitly_wait(2)
        main_page.MenuBtn(self.driver).click()

        # Scroll down in order to click 9-Day Weather Forecast
        self.driver.implicitly_wait(2)
        self.driver.scroll(menu_page.menu_area(self.driver)[6], menu_page.menu_area(self.driver)[1])

        # Click the button of 9-Day Weather Forecast
        self.driver.implicitly_wait(2)
        menu_page.nine_day_forcast_btn(self.driver).click()

        # Verify Forecast of the next 9 days are displayed
        app_first_day = day_weather_forecast_page.day(self.driver)
        cor_anw_ls = self.get_date()
        self.assertEqual(app_first_day.text, cor_anw_ls[0])

        # Check first page: Compare the day between on the 1st page and real days
        for i in range(3):
            item = ('new UiSelector().text("%s")' % cor_anw_ls[i])
            self.driver.implicitly_wait(5)
            app_day = self.driver.find_element_by_android_uiautomator(item)
            self.assertEqual(app_day.text, cor_anw_ls[i])

        # Scroll to the 2nd page
        self.scroll_forecast()

        # # Check the 2nd page day:

        # check the last two items
        for i in range(3, 6):
            item = ('new UiSelector().text("%s")' % cor_anw_ls[i])
            self.driver.implicitly_wait(5)
            app_day = self.driver.find_element_by_android_uiautomator(item)
            self.assertEqual(app_day.text, cor_anw_ls[i])

        # Scroll to the 3rd page
        self.scroll_forecast()

        # Check the 3rd page day:
        for i in range(6, 9):
            if i < 8:
                item = ('new UiSelector().text("%s")' % cor_anw_ls[i])
                self.driver.implicitly_wait(5)
                app_day = self.driver.find_element_by_android_uiautomator(item)
                self.assertEqual(app_day.text, cor_anw_ls[i])
            else:
                item = ('new UiSelector().text("%s")' % cor_anw_ls[i - 7])
                self.driver.implicitly_wait(5)
                app_day = self.driver.find_element_by_android_uiautomator(item)
                self.assertEqual(app_day.text, cor_anw_ls[i - 7])

        sleep(5)
