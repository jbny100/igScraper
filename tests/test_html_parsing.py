import unittest
from igScraper.igScraper import extract_hashtags, parse_content

class TestIgScraper(unittest.TestCase):

	def test_extract_hashtags(self):
		content = "This is a test #tag1 and another #tag2"
		expected_result = "#tag1 #tag2"
		result = extract_hashtags(content)
		self.assertEqual(result, expected_result)

	def test_extract_hashtags_no_hashtage(self):
		content = "This is a test with no hashtags"
		expected_result = ""
		result = extract_hashtags(content)
		self.assertEqual(result, expected_result)

	def test_parse_content(self):
		content = """
		BROKERS: John Doe ~ BUYERS: Jane Doe, Joe Doe ~ UNIT: 10A ~ NOTE FROM BROKER: "Good Deal"
		"""
		expected_result = {
			'tradedny': None,
			'hashtags': '',
			'BROKER': 'John Doe',
			'BUYER': 'Jane Doe, Joe Doe',
			'UNITS': '10A',
			'NOTE': '"Good Deal"'
		}
		result = parse_content(content)
		self.assertEqual(result, expected_result)

		
	def test_parse_content_with_hashtags(self):
		content = """
		BROKERS: John Doe ~ BUYERS: Jane Doe, Joe Doe ~ UNITS: 10A #apartment
		"""
		expected_result = {
			'tradedny': None, 
			'hashtags': '#apartment', 
			'BROKER': 'John Doe', 
			'BUYER': 'Jane Doe, Joe Doe', 
			'UNITS': '10A'
		}

		result = parse_content(content)
		self.assertEqual(result, expected_result)

if __name__ == '__main__':
	unittest.main()


"""In the given test case, we didn't use the setUp() method because 
each test is completely isolated and doesn't rely on any shared state."""



