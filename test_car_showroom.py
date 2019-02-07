import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_adding_a_car(self):
        driver = self.driver
        driver.get("http://salon.rpgit.pl")

        username_input = driver.find_element_by_id("id_username")
        password_input = driver.find_element_by_id("id_password")
        login_button = driver.find_element_by_id("id_login_btn")

        username_input.send_keys("test-user")
        password_input.send_keys("test-password")
        login_button.click()

        # Advanced task (not required):
        # Try to change the time.sleep to a better wait!
        time.sleep(3)

        # TO DO:
        # 1. Click the "Add a car" button.
        # 2. Add a car.
        # 3. Check if the car was added to the list.
        # Your code goes here:
        

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()