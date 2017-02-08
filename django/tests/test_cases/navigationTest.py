import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from __builtin__ import classmethod


class NavigationTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Setting up new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.get('http://localhost:8000/')
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def testNavigation(self):
        # Check student items links
        self.driver.find_element_by_link_text('Rosberg').click()
        result = self.driver.find_element_by_xpath('/html/body/h1')
        self.assertEqual(result.text, 'Edit student 1')
        self.driver.back()
        self.driver.find_element_by_link_text('Nicolas').click()
        result = self.driver.find_element_by_xpath('/html/body/h1')
        self.assertEqual(result.text, 'Edit student 1')
        self.driver.back()
        self.driver.find_element_by_link_text('Raikkonen').click()
        result = self.driver.find_element_by_xpath('/html/body/h1')
        self.assertEqual(result.text, 'Edit student 2')
        self.driver.back()
        self.driver.find_element_by_link_text('Kimmi').click()
        result = self.driver.find_element_by_xpath('/html/body/h1')
        self.assertEqual(result.text, 'Edit student 2')
        self.driver.back()
        self.driver.find_element_by_link_text('Vettel').click()
        result = self.driver.find_element_by_xpath('/html/body/h1')
        self.assertEqual(result.text, 'Edit student 3')
        self.driver.back()
        self.driver.find_element_by_link_text('Sebastian').click()
        result = self.driver.find_element_by_xpath('/html/body/h1')
        self.assertEqual(result.text, 'Edit student 3')
        self.driver.back()


if __name__ == '__main__':
    unittest.main()