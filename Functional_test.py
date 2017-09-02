from selenium import webdriver
import unittest 

class ToDoApp(unittest.TestCase) :
	def setUp(self):
		self.browser =  webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_star_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')

		#She notices the page title and header mention to-do-lists
		self.assertIn('Django', self.browser.title)

if __name__== '__main__' :
	unittest.main()