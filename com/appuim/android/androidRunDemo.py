__author__ = 'Lambert Liu'
import os
import sys
import inspect
from nose.tools import with_setup
from appium import webdriver
from sauceclient import SauceClient

browsers = [{
    'appiumVersion':    '1.3.4',
    'platformName':     'Android',
    'platformVersion':  '4.3',
    'deviceName':       'Android Emulator',
    'app':              'http://appium.s3.amazonaws.com/NotesList.apk',
    'name':             'Python Appium Android 4.3 example'
}, {
    'appiumVersion':    '1.3.4',
    'platformName':     'Android',
    'platformVersion':  '5.0',
    'deviceName':       'Android Emulator',
    'app':              'http://appium.s3.amazonaws.com/NotesList.apk',
    'name':             'Python Appium Android 5.0 example'
}]

username = os.environ['SAUCE_USERNAME']
access_key = os.environ['SAUCE_ACCESS_KEY']

def launchBrowser(caps):
    caps['name'] = inspect.stack()[1][3]
    return webdriver.Remote(
            command_executor = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (username, access_key),
            desired_capabilities = caps);

def teardown_func():
    global driver
    driver.quit()
    sauce_client = SauceClient(username, access_key)
    status = sys.exc_info() == (None, None, None)
    sauce_client.jobs.update_job(driver.session_id, passed=status)

# Will generate a test for each browser and os configuration
def test_generator_verify_google():
    for browser in browsers:
        yield verify_note, browser

@with_setup(None, teardown_func)
def verify_note(browser):
    global driver
    driver = launchBrowser(browser)
    driver.find_element_by_accessibility_id('New note').click()
    driver.find_element_by_class_name('android.widget.EditText').send_keys('Here is a new note from Python')
    driver.find_element_by_accessibility_id('Save').click()
    notes = driver.find_elements_by_class_name('android.widget.TextView')
    assert (notes[2].text == 'Here is a new note from Python'), 'Note failed'