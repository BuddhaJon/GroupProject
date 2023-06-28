import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(., 'Login')]").click()
        user = "parker"
        pwd = "5050"

        user_input = driver.find_element(By.XPATH, "//input[@name='username']")
        pwd_input = driver.find_element(By.XPATH, "//input[@name='password']")

        user_input.send_keys(user)
        pwd_input.send_keys(pwd)
        button = driver.find_element(By.XPATH, "//input[@value='login']")
        button.click()


        try:
            time.sleep(2)
            elem = driver.find_element(By.XPATH,
                                       "//*[contains(text(), 'Logout')]")
            self.driver.close()
            assert True
        except NoSuchElementException:
            driver.close()
            self.fail("About page does not load when clicked")

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()