__author__ = 'proko'

import unittest
import json
import os
from testcases import nine_day_forecast


PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
)

with open(PATH('../config_collection/device_settings.json'), 'r') as f:
    data = json.load(f)

if __name__ == '__main__':
    # In order to add more test cases in the future, I adopt test suite.
    suite_list = [nine_day_forecast.NineDayForecast, ]
    for test in suite_list:
        suite = unittest.TestLoader().loadTestsFromTestCase(test)
        unittest.TextTestRunner(verbosity=2).run(suite)