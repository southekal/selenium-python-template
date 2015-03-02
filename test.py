import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://docs.seleniumhq.org/projects/webdriver/")

    def test_search_selenium_page(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "title doesn't match."
        main_page.search_text_element = "selenium"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()