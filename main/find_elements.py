from lib2to3.pgen2 import driver
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import keyboard

class HelloWorld(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../resources/chromedriver')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field= self.driver.find_element_by_id('search')

    
        
    def test_search_book(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('Book')
        search_field.submit()
        books = driver.find_elements_by_css_selector('ul>li>div>h2>a')
        self.assertEqual(3, len(books))

    # def test_search_test_field_by_name(self):
    #     search_field = self.driver.find_element_by_name('q')

    # def test_search_test_field_by_class_name(self):
    #     search_field = self.driver.find_elements_by_class_name('input-text')

    # def test_button_search_enabled(self):
    #     button_search = self.driver.find_elements_by_class_name('button')

    # def test_count_banners(self):
    #     banner_list = self.driver.find_element_by_class_name('promos')
    #     banners = banner_list.find_elements_by_tag_name('img')
    #     self.assertEqual(3, len(banners))

    # def test_image_man_xpath(self):
    #     image_man = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    # def test_shopping_cart(self):
    #     shopping_cart = self.driver.find_element_by_css_selector('div.header-minicart span.icon')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'find_elements', report_name = 'report_find_elements'))