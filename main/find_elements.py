from lib2to3.pgen2 import driver
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import keyboard

class HelloWorld(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../resources/chromedriver')
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('user-name')
        search_field.send_keys('standard_user')
        # self.driver.find_element_by_id('password')
        # search_field.send_keys('secret_sauce')
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'find_elements', report_name = 'report_find_elements'))