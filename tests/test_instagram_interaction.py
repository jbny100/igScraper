import unittest
from selenium import webdriver
from igScraper import login, load_profile, scroll_down, click_on_post, parse_post

class TestIgScraper(unittest.TestCase):

	def setUp(self):
		# Set up Instagram credentials for testing purposes.
		self.username = 'turnkeyofficespace'
		self.password = 'Cv3+;37VUnG&'
		self.profile = 'https://www.instagram.com/tradedny'
		self.browser = webdriver.Firefox()

	def tearDown(self):
		# This method will be called after every test.
		# Use it to clean up any resources the tests used.
		self.browser.quit()

	def test_login(self):
		try:
			# Call the login function.
			login(self.browser, self.username, self.password)
		except Exception as e:
			self.fail(f"login() raised Exception unexpectedly: {e}")

	def test_load_profile(self):
		try:
			# Call the load_profile function
			load_profile(self.browser, self.profile)
		except Exception as e:
			self.fail(f"load_profile() raised Exception unexpectedly: {e}")
	
	def test_scroll_down(self):
		try:
			# Call the scroll_down function
			scroll_down(self.browser)
		except Exception as e:
			self.fail(f"scroll_down() raised Exception unexpectedly: {e}")

	def click_on_post(self):
		try:
			# Call the click_on_post function
			click_on_post(self.browser, ".img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3")
		except exception as e:
			self.fail(f"click_on_post() raised Exception unexpectedly: {e}")

	def test_parse_post(self):
		try:
			# Call the parse_post function
			parse_post(self.browser)
		except Exception as e:
			self.fail(f"parse_post() raised Exception unexpectedly: {e}")


if __name__ == '__main__':
	unittest.main()



