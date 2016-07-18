# PYAndroid_Test
*PyCharm 使用python语言针对Android 做APPIUM或uiautomator测试*
##引入库
from uiautomator import device as d

##添加用例

    def test__idlescreen_settings(self):
        print("quick settings")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)
        d.open.quick_settings()
        time.sleep(2)
