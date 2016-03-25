__author__ = 'Lambert Liu'

import unittest
import time
from uiautomator import device as d



class KazamTestCase(unittest.TestCase):


    def setUp(self):
        self.seq = range(10)

    def phone_call10010(self):
        d.press.back()
        time.sleep(1)
        d.press.home()
        time.sleep(1)
        print("")
        if d(text="Phone").exists:
            print("Test Phone app")
            d(text="Phone").click()
            time.sleep(2)
            d(text="1").click()
            time.sleep(1)
            d(text="0").click()
            time.sleep(1)
            d(text="0").click()
            time.sleep(1)
            d(text="1").click()
            time.sleep(1)
            d(text="0").click()
            d(className="android.widget.LinearLayout", resourceId="com.android.dialer:id/dialButtonContainer")\
                .child(description="dial",className="android.widget.ImageButton").click()
            time.sleep(5)
            if d(text="OK").exists:
                print("No SIM or No network")
                d(text="OK").click()
            else:
                d(description="End",className="android.widget.ImageButton").click()

            time.sleep(2)
            print("Finish the test")
        else:


            print("Phone not exists")

        d.press.back()
        time.sleep(1)
        d.press.home()

    def mms_add_picture(self):
        print("")
        if d(text="Messaging").exists:
            print("")
            d(text="Messaging").click()
            time.sleep(2)
            d(description="New message",className="android.widget.TextView").click()
            time.sleep(2)
            d(className="android.widget.ImageButton", resourceId="com.android.mms:id/share_button").click()
            time.sleep(2)
            d(text="Capture picture").click()
            time.sleep(2)
            d(className="android.widget.ImageView",resourceId="com.android.gallery3d:id/shutter_button_photo",description="Shutter button").long_click()
            time.sleep(5)
            d(className="android.widget.ImageView",description="OK").click()
            time.sleep(2)
            # d(text="Type name or number").settext("10010")
            # time.sleep(2)
            # d.press.back()
            # time.sleep(1)
            d.press.back()
            time.sleep(1)
            if d(text="OK",className="android.widget.Button").exists:
                d(text="OK",className="android.widget.Button").click()
                time.sleep(2)
                d.press.back();

            else:
                d.press.home()
            d.press.home()
    def camera_take_picture(self):
        print("-----------")
        if d(text="Camera").exists:
            d(text="Camera").click()
            time.sleep(2)
            d(description="Shutter button",className="android.widget.ImageView").click()
            time.sleep(4)
            d(description="Shutter button",className="android.widget.ImageView").long_click()
            time.sleep(20)
            d(description="Video shutter button",className="android.widget.ImageView").click()
            time.sleep(4)
            d(description="Video shutter button",className="android.widget.ImageView").click()
            time.sleep(4)

            d.press.back()
            time.sleep(2)
            d.press.home()




    def launcher_Common_APP(self):
        arr = ["Camera","Chrome","Messaging","Phone"]
        print("---------------------")
        for i in range(0, 4):
            print("Test "+arr[i])
            d(text=arr[i]).click()
            time.sleep(2)
            d.press.back()
            time.sleep(1)
            d.press.home()
            time.sleep(1)











if __name__ == '__main__':
    unittest.main()
