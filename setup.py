from selenium import webdriver

class WebDriver(object):
	def __init__(self):
		self.driver = None

	def setUp(self):
		print 'getting driver'
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()

	def tearDown(self):
		self.driver.close()
		self.driver.quit()

# if __name__ == "__main__":
# 	WebDriver()