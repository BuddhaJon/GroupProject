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
        user = "parker"
        pwd = "5050"
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[contains(., 'About')]").click()

        time.sleep(3)
        try:
            elem = driver.find_element(By.XPATH, "//*[contains(text(), 'Jonathan is an avid techie with a love for mindfulness')]")
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