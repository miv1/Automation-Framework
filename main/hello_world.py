from unittest import main
from unittest import TestCase
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = '../resources/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.google.com.bo')

    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    main(verbosity = 2, testRunner = HTMLTestRunner(output = 'hello_world', report_name = 'report_hello_world'))