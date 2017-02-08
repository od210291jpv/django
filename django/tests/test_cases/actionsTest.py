import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from __builtin__ import classmethod


class ActionsTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        time.sleep(10)
        cls.driver.implicitly_wait(30)
        cls.driver.get('http://localhost:8000/')
        cls.driver.maximize_window()

    def testActions(self):
        # Finding on navbar elements
        students = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/ul/li[1]/a')
        attendance = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/ul/li[2]/a')
        group = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/ul/li[3]/a')
        # Check if links are visible
        self.assertTrue(students.is_displayed())
        self.assertTrue(attendance.is_displayed())
        self.assertTrue(group.is_displayed())
        # Clicking on navbar elements
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/ul/li[1]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/ul/li[3]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/ul/li[1]/a').click()
        # Check sorting links
        # Finding first sorting link
        sort_by_surname = self.driver.find_element_by_xpath('/html/body/div/div[3]/div/table/thead/tr/th[3]/a')
        # Finding list of a students
        students_list = self.driver.find_elements_by_xpath('/html/body/div/div[3]/div/table/tbody/tr')
        # Checking if students list lenth is equal = 3
        self.assertEqual(len(students_list), 3)
        # Asserting first student's name
        first_student_name = students_list[0].find_element_by_link_text('Rosberg')
        self.assertEqual(first_student_name.text, 'Rosberg')
        # Performing sorting by name
        sort_by_surname.click()
        students_list = self.driver.find_elements_by_xpath('/html/body/div/div[3]/div/table/tbody/tr')
        first_student_name = students_list[0].find_element_by_xpath\
            ('/html/body/div/div[3]/div/table/tbody/tr[1]/td[3]/a')
        self.assertEqual(first_student_name.text, 'Kartekiyan')

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
