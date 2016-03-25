__author__ = 'Lambert Liu'
#coding=utf-8
__author__ = 'Junior'

from appium import webdriver
import random
import time





import unittest

class reproduceblackscreen(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {}#这里其实也可以把下面的参数,放到caps里面,通过字典的结构模式
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '6.0'

        self.desired_caps['deviceName'] = 'FENZSOU4IBP7UG4D'
        self.desired_caps['appPackage'] = 'com.fxly.appinfo.apps'
        self.desired_caps['appActivity'] = '.AppsActivity'

    def test_reproduce(self):

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)#默认写法

        def timewait(int):
            self.driver.implicitly_wait(int)


        timewait(20)
        self.driver.switch_to_alert()

        self.driver.find_element_by_id('com.shishike.calm:id/negative_button').click()
        timewait(1)
        #下面就开始找元素找点了
        self.driver.find_element_by_name('admin').click()
        timewait(1)

        i=1
        for i in range(1,7):
            self.driver.find_element_by_id('com.shishike.calm:id/eight').click()
            i=i+1

            timewait(1)


        self.driver.find_element_by_xpath("//android.widget.GridView[1]/android.widget.LinearLayout[2]/android.widget.ImageView[1]").click()

        timewait(1)

        n=random.randint(0,20)
        for x in range(n):
            self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.GridView[1]/android.widget.FrameLayout[9]").click()
            timewait(10)

            self.driver.find_element_by_id('com.shishike.calm:id/btn_order_dish_right_cash').click()
            timewait(10)

            self.driver.find_element_by_name('扫码').click()
            timewait(10)
            self.driver.find_element_by_name('二维码').click()
            timewait(10)

            self.driver.find_element_by_id('com.shishike.calm:id/pay_back').click()
            timewait(3)

            self.driver.find_element_by_id('com.shishike.calm:id/cashier_title_bar_menu_btn').click()
            timewait(3)

            self.driver.find_element_by_id('com.shishike.calm:id/ordercenter').click()
            timewait(3)

            self.driver.find_element_by_id('com.shishike.calm:id/un_payment').click()
            timewait(3)

            self.driver.find_element_by_id('com.shishike.calm:id/unpay_order_detail_un_use').click()
            timewait(3)


            self.driver.switch_to_alert()
            timewait(3)

            self.driver.find_element_by_name('作废').click()
            # self.driver.find_element_by_xpath("////android.widget.Button[1]").click()
            timewait(3)


            self.driver.find_element_by_id('com.shishike.calm:id/cashier_title_bar_menu_btn').click()
            timewait(3)

            self.driver.find_element_by_id('com.shishike.calm:id/orderdishes').click()
            timewait(3)

            x=x+1

    def tearDown(self):
        self.driver.quit()
#添加用例执行脚本
if __name__ == "__main__":
    case=unittest.TestLoader().loadTestsFromTestCase(reproduceblackscreen)

    unittest.TextTestRunner(verbosity=3).run(case)