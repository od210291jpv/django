import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from xmlrunner import xmlrunner

# Importing test classes
from actionsTest import ActionsTest
from navigationTest import NavigationTest

# Loading tests
test1 = unittest.TestLoader().loadTestsFromTestCase(ActionsTest)
test2 = unittest.TestLoader().loadTestsFromTestCase(NavigationTest)

# Creating test suite
test_suite = unittest.TestSuite([test1, test2])

# Run the suite
# unittest.TextTestRunner(verbosity=2).run(test_suite)

# Run test suite with xmlrunner
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(test_suite)

