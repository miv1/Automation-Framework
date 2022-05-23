from cgi import test
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):    

    def test_remove_item(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()
        user_field = driver.find_element(by=By.ID, value='user-name')
        user_field.send_keys('standard_user')
        psw_field = driver.find_element(by=By.ID, value='password')
        psw_field.send_keys('secret_sauce')        
        login_btn = driver.find_element(by=By.ID, value='login-button')
        login_btn.click()        
        cart_icon = driver.find_element(by=By.CLASS_NAME, value='shopping_cart_link')
        add_cart_backpack_btn = driver.find_element(by=By.ID, value='add-to-cart-sauce-labs-backpack')
        add_cart_backpack_btn.click()
        shopping_cart_badge_btn = driver.find_element(by=By.CLASS_NAME, value='shopping_cart_badge')
        self.assertTrue(shopping_cart_badge_btn, shopping_cart_badge_btn)
        remove_cart_backpack_btn = driver.find_element(by=By.ID, value='remove-sauce-labs-backpack')
        remove_cart_backpack_btn.click()    
        self.assertIsNot(cart_icon, 1, "No number added")
        self.assertTrue(add_cart_backpack_btn, add_cart_backpack_btn)
        driver.quit()

    def test_display_selected_item(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()
        user_field = driver.find_element(by=By.ID, value='user-name')
        user_field.send_keys('standard_user')
        psw_field = driver.find_element(by=By.ID, value='password')
        psw_field.send_keys('secret_sauce')        
        login_btn = driver.find_element(by=By.ID, value='login-button')
        login_btn.click()        
        cart_icon = driver.find_element(by=By.CLASS_NAME, value='shopping_cart_link')
        add_cart_backpack_btn = driver.find_element(by=By.ID, value='add-to-cart-sauce-labs-backpack')
        add_cart_backpack_btn.click()
        cart_icon.click()
        item_selected = driver.find_element(by=By.ID, value='item_4_title_link')
        self.assertTrue(item_selected, item_selected)
        driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'test_interview', report_name = 'report_test_interview'))
    