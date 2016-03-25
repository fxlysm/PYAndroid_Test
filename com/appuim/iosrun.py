__author__ = 'Lambert Liu'
import os, unittest
from appium import webdriver

class StoryIos01(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'iOS'
		desired_caps['platformVersion'] = '8.1'
		desired_caps['deviceName'] = 'iPhone 6'
		desired_caps['app'] = os.path.join(
			'/Users/mesutgunes/Projects/mobile_automation/appium/appium-ios-automation-sample/apps/GooglePlusPlatformSample.app'
			)

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	def tearDown(self):
		# each test case will start from begining
		self.driver.quit()

	def test_open_application(self):
		self.assertTrue(self.driver.find_element_by_name("Sign in"))

	def test_sign_in_button(self):
		self.driver.find_element_by_name("Sign in")
		self.driver.find_element_by_name("Sign in").click()
		self.assertTrue(self.driver.find_element_by_id("Back"))

		self.driver.find_element_by_id("Back").click()
		self.assertTrue(self.driver.find_element_by_name("Sign in"))

	def test_share_button(self):
		self.driver.find_element_by_id("Share")
		self.driver.find_element_by_id("Share").click()
		self.assertTrue(self.driver.find_element_by_name("Pre-fill text"))

		self.driver.find_element_by_name("Pre-fill text").click()
		self.assertTrue(self.driver.find_element_by_name("share_view_text_view"))

		self.driver.find_element_by_name("share_view_text_view").clear()
		self.driver.find_element_by_name("share_view_text_view").send_keys("yuppie!")
		self.driver.find_element_by_name("share_view_text_view").send_keys("\n\n       Appium rocks!")
		self.assertTrue("yuppie!" in self.driver.find_element_by_name("share_view_text_view").text)


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(StoryIos01)
	unittest.TextTestRunner(verbosity=2).run(suite)
