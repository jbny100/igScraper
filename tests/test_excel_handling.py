
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import os
import unittest
from openpyxl import load_workbook
from igScraper.igScraper import save_data
from pandas.testing import assert_frame_equal

chrome_options = Options()
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_path = '/Users/jonathanbachrach/Documents/Automate/TradedScrape/chromedriver'

class TestIgScraper(unittest.TestCase):

	def setUp(self):
		# This method will be called befor every test.
		# Use it to set up any state that your tests need.
		self.browser = browser = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
		self.data = [{'username': 'test_user', 'followers': 123, 'following': 321}]
		self.headers = ['username', 'followers', 'following']
		self.sheet = 'sheet1'

	def tearDown(self):
		# This method will be called after every test.
		# Use it to clean up any resources the tests used.
		if os.path.exists('test.xlxs'):
			try:
				os.remove('test.xlsx')
			except PermissionError:
				print("Unable to remove file: Permission denied")

	def test_save_data(self):
		# A test case for the save_data function.
		for item in self.data:
			save_data(item, 'test.xlsx', self.headers, self.sheet)

		# Read the data from the Excel file.
		df = pd.read_excel('test.xlsx')
		expected_df = pd.DataFrame(self.data)
		assert_frame_equal(df, expected_df)


	def test_save_data_empty(self):
		# Test case to check if the function handles empty data properly.
		empty_data = []

		with self.assertRaises(ValueError):
			save_data(empty_data, 'test.xlsx', self.headers, self.sheet)


	def test_save_data_invalid(self):
		# Test case to check if the function handles invalid data properly.
		invalid_data = 'invalid_data'

		with self.assertRaises(TypeError):
			save_data(self.browser, invalid_data, 'test.xlsx', self.headers, self.sheet)


if __name__ == '__main__':
	unittest.main()


