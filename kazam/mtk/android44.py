__author__ = 'Lambert Liu'

import unittest
import time
from uiautomator import device as d


d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait").click(text="Close")
d.watcher("AUTO_FC_WHEN_ANR").triggered
d.watcher("APP_CRASH").when(text="Unfortunately, Settings has stopped.").when(text="Wait").click(text="OK")
d.watcher("APP_CRASH").triggered

class IdleScreenTestCase(unittest.TestCase):


    def setUp(self):
        self.seq = range(10)
    print("Test idle screen")
    d.press.back()
    time.sleep(2)
    d.press.home()
    time.sleep(2)
    # def test_Power_off_on(self):
    #     if d.screen.off():
    #         time.sleep(1)
    #         d.wakeup()
    #         time.sleep(4)
    #     d.long_press.power()
    #     time.sleep(4)
    #     d(text="Reboot",className="android.widget.TextView").click()
    #     time.sleep(40)
    #     d.press.home()
    #     time.sleep(2)
    def  test_idlescreen_lock_screen(self):
        print("Test Lock screen")
        if d.screen == "off":
            d.wakeup()
            time.sleep(4)

        for i in range(0, 5):
           d.press.power()
           time.sleep(2)
           d.wakeup()
           time.sleep(3)

    def test__idlescreen_settings(self):
        print("quick settings")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)
        d.open.quick_settings()
        time.sleep(2)

    def test_idlescreen_swipe(self):
        print("Swipe on idlescreen")
        d.swipe(300, 480, 480, 20, steps=10)
        time.sleep(2)
        d.swipe(300, 480, 480, 20, steps=10)
        time.sleep(2)


class PhoneTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    d.press.back()
    time.sleep(2)
    d.press.home()
    time.sleep(2)
    def test_phone_call10010(self):
        d.press.back()
        time.sleep(1)
        d.press.home()
        time.sleep(1)

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

    def test_calllogs(self):
        print("Test call logs")
        d.press.home()
        time.sleep(2)
        if d(text="Phone").exists:
            d(text="Phone").click()
            time.sleep(2)
            if d(description="Call History",className="android.widget.ImageButton", resourceId="com.android.dialer:id/call_history_on_dialpad_button").exists:
                print("Enter Call history Main screen")
                d(description="Call History",className="android.widget.ImageButton", resourceId="com.android.dialer:id/call_history_on_dialpad_button").click()
                time.sleep(3)
                if d(className="android.widget.LinearLayout", resourceId="com.android.dialer:id/calllog_search_button_cluster").child(
                    className="android.widget.Button", resourceId="com.android.dialer:id/btn_type_filter_incoming").exists:
                    print("Enter  Incoming screen")
                    d(className="android.widget.Button", resourceId="com.android.dialer:id/btn_type_filter_incoming").click()
                    time.sleep(2)

                else:
                    print("No found incoming")

                if d(className="android.widget.Button", resourceId="com.android.dialer:id/btn_type_filter_outgoing").exists:
                    print("Enter Outgoing screen")
                    d(className="android.widget.Button", resourceId="com.android.dialer:id/btn_type_filter_outgoing").click()
                    time.sleep(2)
                else:
                    print("No found Outgoing screen")

                if d(className="android.widget.Button", resourceId="com.android.dialer:id/btn_type_filter_missed").exists:
                    print("Enter Missed screen")
                    d(className="android.widget.Button", resourceId="com.android.dialer:id/btn_type_filter_missed").click()
                    time.sleep(2)
                else:
                    print("No found Missed button")
                d.press.menu()
                time.sleep(2)

                if d(text="Delete").exists:
                    print("Del Call logs")
                    d(text="Delete").click()
                    time.sleep(2)
                    while d(className="android.widget.CheckBox",checked="false").exists:
                        d(className="android.widget.CheckBox",checked="false").click()
                        time.sleep(2)
                    d(text="OK").click()
                    time.sleep(2)

                else:
                    print("Calllogs is null")

            else:
                print("No found Call history button")

        else:
            print("No found Phone APP")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)

    def test_Emergency_call(self):
        print("Test Emergency call")
        d.press.back()
        time.sleep(1)
        d.press.home()
        time.sleep(1)
        if d(text="Phone").exists:
            print("Emergency call 112")
            d(text="Phone").click()
            d(text="1").click()
            time.sleep(1)
            d(text="1").click()
            time.sleep(1)
            d(text="2").click()
            d(className="android.widget.LinearLayout", resourceId="com.android.dialer:id/dialButtonContainer")\
                .child(description="dial",className="android.widget.ImageButton").click()
            time.sleep(8)
            d(description="End",className="android.widget.ImageButton").click()

            time.sleep(2)
            print("Emergency call 911")
            d(text="9").click()
            time.sleep(1)
            d(text="1").click()
            time.sleep(1)
            d(text="1").click()
            d(className="android.widget.LinearLayout", resourceId="com.android.dialer:id/dialButtonContainer")\
                .child(description="dial",className="android.widget.ImageButton").click()
            time.sleep(8)
            d(description="End",className="android.widget.ImageButton").click()

            time.sleep(2)

            print("Emergency call 999")
            d(text="9").click()
            time.sleep(1)
            d(text="9").click()
            time.sleep(1)
            d(text="9").click()
            d(className="android.widget.LinearLayout", resourceId="com.android.dialer:id/dialButtonContainer")\
                .child(description="dial",className="android.widget.ImageButton").click()
            time.sleep(8)
            if d(description="End",className="android.widget.ImageButton").exists:
                d(description="End",className="android.widget.ImageButton").click()
                time.sleep(2)
            else:
                print("Not support 999")

            time.sleep(2)

            print("Emergency call 998")
            d(text="9").click()
            time.sleep(1)
            d(text="9").click()
            time.sleep(1)
            d(text="8").click()
            d(className="android.widget.LinearLayout", resourceId="com.android.dialer:id/dialButtonContainer")\
                .child(description="dial",className="android.widget.ImageButton").click()
            time.sleep(8)
            if d(description="End",className="android.widget.ImageButton").exists:
                d(description="End",className="android.widget.ImageButton").click()
                time.sleep(2)
            else:
                print("Not support 998")

            time.sleep(2)

            print("Emergency call 997")
            d(text="9").click()
            time.sleep(1)
            d(text="9").click()
            time.sleep(1)
            d(text="7").click()
            d(className="android.widget.LinearLayout", resourceId="com.android.dialer:id/dialButtonContainer")\
                .child(description="dial",className="android.widget.ImageButton").click()
            time.sleep(8)
            if d(description="End",className="android.widget.ImageButton").exists:
                d(description="End",className="android.widget.ImageButton").click()
                time.sleep(2)
            else:
                print("Not support 997")

            time.sleep(2)

            print("Emergency call 986")
            d(text="9").click()
            time.sleep(1)
            d(text="8").click()
            time.sleep(1)
            d(text="6").click()
            d(className="android.widget.LinearLayout", resourceId="com.android.dialer:id/dialButtonContainer")\
                .child(description="dial",className="android.widget.ImageButton").click()
            time.sleep(8)
            if d(description="End",className="android.widget.ImageButton").exists:
                d(description="End",className="android.widget.ImageButton").click()
                time.sleep(2)
            else:
                print("Not support 986")

            time.sleep(2)
        else:
            print("No found Phone App")

        d.press.back()
        time.sleep(1)
        d.press.home()
        time.sleep(2)

    def test_USSD(self):
        print("Test USSD")
        d.press.back()
        time.sleep(1)
        d.press.home()
        time.sleep(1)

        if d(text="Phone").exists:
            print("Test Phone app")
            d(text="Phone").click()
            time.sleep(2)
            d(text="*").click()
            time.sleep(1)
            d(text="#").click()
            time.sleep(1)
            d(text="2").click()
            time.sleep(1)
            d(text="1").click()
            time.sleep(1)
            d(text="#").click()
            d(className="android.widget.LinearLayout", resourceId="com.android.dialer:id/dialButtonContainer")\
                .child(description="dial",className="android.widget.ImageButton").click()
            time.sleep(5)
            if d(text="Call forwarding").exists:
                print("No SIM or No network")
                d(text="OK").click()
                time.sleep(2)
            else:
                d(text="OK").click()

            time.sleep(2)
            print("Finish the test")
        else:
            print("Phone not exists")

        d.press.back()
        time.sleep(1)
        d.press.home()


class MMSTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    d.press.back()
    time.sleep(2)
    d.press.home()
    time.sleep(2)
    def test_mms_add_picture(self):

        if d(text="Messaging").exists:
            print("Test add MMS")
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

    def test_mms_setting(self):
        print("Test MMS Settings")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)
        if d(text="Messaging").exists:
            d(text="Messaging").click()
            time.sleep(2)
            d.press.menu()
            time.sleep(2)
            if d(text="Settings",className="android.widget.TextView",resourceId="android:id/title").exists:
                d(text="Settings",className="android.widget.TextView",resourceId="android:id/title").click()
                time.sleep(2)
                if d(text="Multimedia Message (MMS)",className="android.widget.TextView",resourceId="android:id/text1").exists:
                    d(text="Multimedia Message (MMS)",className="android.widget.TextView",resourceId="android:id/text1").click()
                    time.sleep(2)
                    sms_settings_menu=["Group messaging","Delivery reports","Auto-retrieve","Roaming auto-retrieve"];
                    for i in range(0, 4):
                        if d(text=sms_settings_menu[i],className="android.widget.TextView").exists:
                            d(text=sms_settings_menu[i],className="android.widget.TextView").click()
                            print("click "+sms_settings_menu[i])
                            time.sleep(2)

                        else:
                            print("No found "+sms_settings_menu[i])
                else:
                    print("No found Multimedia Message (MMS) ")
                d.press.back()
                time.sleep(2)
            else:
                print("No found MMS settings menu")
            d.press.back()
            time.sleep(2)
        else:
            print("No found Message APP")
        d.press.back()
        time.sleep(2)

class SMSTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    d.press.back()
    def test_add_sms(self):
        print("Test Add SMS")

    def test_sms_settings_input_mode(self):
        print("SMS-----input mode")

    def test_sms_settings_size_limit(self):
        print("SMS-----Sms size limit for converting to mms")

    def test_sms_settings_manage_sim_message(self):
        print("SMS-----Manage SIM card message")

    def test_sms_settings_delivery_report(self):
        print("SMS-----Manage SIM card message")

    def test_sms_settings_other(self):
        print("SMS-----Other settings")

class LauncherTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    d.press.back()
    time.sleep(2)
    d.press.home()
    time.sleep(2)
    def test_launcher_Common_APP(self):
        arr = ["Camera","Chrome","Messaging","Phone"]
        print("----Launcher common APP-------")
        for i in range(0, 4):
            print("Test Launcher view "+arr[i])
            if d(text=arr[i],className="android.widget.TextView").exists:
                d(text=arr[i],className="android.widget.TextView").click()
            else:
                print("Not found "+arr[i])

            time.sleep(2)
            d.press.back()
            time.sleep(1)
            d.press.home()
            time.sleep(1)

    def test_launcher_widgets(self):
        print("Test Widgets")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)
        d.press.menu()
        if d(text="Widgets",className="android.widget.TextView", resourceId="com.android.launcher3:id/widget_button").exists:
            print("Found Widgets")
            d(text="Widgets",className="android.widget.TextView", resourceId="com.android.launcher3:id/widget_button").click()
            time.sleep(2)
            while not d(text="Email",className="android.widget.TextView", resourceId="com.android.launcher3:id/widget_name").exists:
                d.swipe(400, 500, 50, 500, steps=50);
            if d(className="android.widget.LinearLayout").child(text="Email",className="android.widget.TextView", resourceId="com.android.launcher3:id/widget_name").exists:
                print("swipe email widget to launcher")
                d.drag(360, 200, 480, 200, steps=100)
                time.sleep(2)
                if d(text="Choose folder",className="android.widget.TextView", resourceId="android:id/action_bar_title").exists:
                    print("choose inbox folder for email")
                    d(text="Inbox",className="android.widget.TextView", resourceId="com.android.email:id/name").click()
                    time.sleep(2)
                else:
                    print("drap email widget to launcher fail")
            else:
                print("No found email widget")
            d.press.back()
            time.sleep(2)

        else:
            print("No found widgets button")
        d.press.back()
        time.sleep(2)

    def test_launcher_wallpaper(self):
        print("Test Wallpaper")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)
        d.press.menu()
        if d(text="Wallpaper",className="android.widget.TextView", resourceId="com.android.launcher3:id/widget_button").exists:
            print("Found wallpaper")
            d(text="Wallpaper",className="android.widget.TextView", resourceId="com.android.launcher3:id/widget_button").click()
            time.sleep(2)
            if d(text="Set wallpaper",className="android.widget.TextView").exists:
                print("Set wallpaper")
                d(text="Set wallpaper",className="android.widget.TextView").click()
                time.sleep(2)
            else:
                print("No found set button")

        else:
            print("No found wallpaper")
        d.press.back()
        time.sleep(2)

class CameraTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    d.press.back()
    time.sleep(2)
    d.press.home()
    time.sleep(2)
    def test_camera_take_picture(self):
        print("-----Camera  Take  pickture/ Recording video-----")
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

class EmailTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    print("Start Test Email")
    d.press.back()
    time.sleep(2)
    d.press.home()
    time.sleep(2)

    def test_add_email_account(self):
        print("Test Add email account")
        d(className="android.view.View",resourceId="com.android.launcher3:id/layout").\
            child(description="Apps",className="android.widget.TextView").click()
        while not d(text="Email",className="android.widget.TextView").exists:
            d.drag(600, 480, 50, 480, steps=100);
            time.sleep(2)
        d(text="Email",className="android.widget.TextView").click()
        time.sleep(2)
        if d(text="Account setup",className="android.widget.TextView").exists:
            print("Frist add email account")
            d(text="Email address",className="android.widget.MultiAutoCompleteTextView",resourceId="com.android.email:id/account_email").settext("lambert.liu_sz@outlook.com")
            time.sleep(2)
            d(description="Password",className="android.widget.EditText",resourceId="com.android.email:id/account_password").settext("liu3763455")
            time.sleep(2)
            d(text="Next",className="android.widget.Button",resourceId="com.android.email:id/next").click()
            time.sleep(4)
            if d(text="Couldn't open connection to server.",className="android.widget.TextView",resourceId="android:id/message").exists:
                print("No network or some other error")
                d.press.back()
                time.sleep(2)
                # d(text="Couldn't finish",className="android.widget.TextVNiew",resourceId="android:id/alertTitle").click()
            if d(text="Power saving option",className="android.widget.TextView",resourceId="android:id/message").exists:
                print("")
                d(text="OK").click()
                time.sleep(2)
            d(text="Next",className="android.widget.Button",resourceId="com.android.email:id/next").click()
            time.sleep(2)
            d(text="Next",className="android.widget.Button",resourceId="com.android.email:id/next").click()
            time.sleep(2)


        else:
            print("Email have other account")
            d.press.menu()
            time.sleep(2)
            d(test="Settings").click()
            time.sleep(2)
            if d(text="Add account").exists:
                d(text="Add account").click()
                print("add other email account")
                time.sleep(2)
                d(text="Email address",className="android.widget.MultiAutoCompleteTextView",resourceId="com.android.email:id/account_email").settext("lambert.liu_sz@outlook.com")
                time.sleep(2)
                d(description="Password",className="android.widget.EditText",resourceId="com.android.email:id/account_password").settext("liu3763455")
                time.sleep(2)
                d(text="Next",className="android.widget.Button",resourceId="com.android.email:id/next").click()
                time.sleep(2)
                if d(text="Couldn't open connection to server.",className="android.widget.TextView",resourceId="android:id/message").exists:
                    d.press.back()
                    time.sleep(2)
                if d(text="Power saving option",className="android.widget.TextView",resourceId="android:id/message").exists:
                    d(text="OK").click()
                    time.sleep(2)
                d(text="Next",className="android.widget.Button",resourceId="com.android.email:id/next").click()
                time.sleep(2)
                d(text="Next",className="android.widget.Button",resourceId="com.android.email:id/next").click()
                time.sleep(2)


    d.press.back()
    time.sleep(2)



    def test_edit_new_email(self):
        print("Test Add email account")
        d(className="android.view.View",resourceId="com.android.launcher3:id/layout").\
            child(description="Apps",className="android.widget.TextView").click()
        while not d(text="Email",className="android.widget.TextView").exists:
             d.drag(600, 480, 50, 480, steps=100);
             print("Finding Email APP")
        d(text="Email",className="android.widget.TextView").click()
        time.sleep(2)



class SettingsTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    d.press.back()
    time.sleep(2)
    d.press.home()
    time.sleep(2)
    print("Start Test Settings")

    def test_settings_view(self):
        d.press.home()
        time.sleep(2)
        d.press.menu()
        time.sleep(2)
        d(text="Settings",className="android.widget.TextView", resourceId="com.android.launcher3:id/settings_button").click()
        time.sleep(2)
        arr =["Bluetooth","Data usage","Audio profiles","Display","Storage","Battery","Apps","Location","Security","Accessibility","Printing","About phone"]

            #            "Language & input","Backup & reset","Add account","Date & time","Scheduled power on & off","Accessibility","Printing","About phone"]
            #
        for i in range(0, 12):
            if  d(text=arr[i],className="android.widget.TextView").exists:
                print("View "+arr[i])

            else:
                while not d(text=arr[i],className="android.widget.TextView").exists:
                    # print()
                    d.drag(100, 350, 100, 50, steps=100)


            d(text=arr[i],className="android.widget.TextView").click()

            if d(text="Unfortunately, Settings has stopped.").exists:
                print("When runing "+arr[i]+",Settings Crash")
                d(text="OK").click()
                return
            time.sleep(2)
            d.press.back()
            time.sleep(2)



    def test_settings_wifi(self):
        print("Test Settings---Wifi")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)


    def test_settings_bluetooth(self):
        print("Test Settings---Bluetooth")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)

    def test_settings_datausage(self):
        print("Test Settings---Data usage")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)


    def test_settings_more(self):
        print("Test Settings---More")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)

    def test_settings_audioprofiles(self):
        print("Test Settings---Audio profiles")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)

    def test_settings_display(self):
        print("Test Settings---Display")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)


    def test_settings_storage(self):
        print("Test Settings---Storage")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)

    def test_settings_battery(self):
        print("Test Settings---Battery")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)

    def test_settings_apps(self):
        print("Test Settings---Apps")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)

class FMTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def testruningFM(self):
        print("Test FM")
        d.press.back()
        time.sleep(2)
        d.press.back()
        time.sleep(2)
        d(className="android.view.View",resourceId="com.android.launcher3:id/layout").\
            child(description="Apps",className="android.widget.TextView").click()
        if d(text="FM Radio",className="android.widget.TextView").exists:
            d(text="FM Radio",className="android.widget.TextView").click()
            time.sleep(2)
            if d(text="FM",className="android.widget.TextView",resourceId="com.mediatek.FMRadio:id/text_fm").exists:
                print("Phone inset earset,can test FM")
                d.press.menu()
                time.sleep(2)
                d(text="Search",className="android.widget.TextView",resourceId="android:id/title").click()
                time.sleep(10)
                if d(text="Channel list",resourceId="android:id/action_bar_title",className="android.widget.TextView").exists:
                    print("Enter Channel list")
                    if d(text="OK").exists:
                        d(text="OK").click()
                        time.sleep(2)
                    else:
                        print("No OK button")
                    d.press.back()
                    time.sleep(2)
                    print("Back FM main Screen")
                d.press.menu()
                time.sleep(2)
                if d(text="Speaker",className="android.widget.TextView",resourceId="android:id/title").exists:
                    print("Test Speaker")
                    d(text="Speaker",className="android.widget.TextView",resourceId="android:id/title").click()
                    time.sleep(2)
                d.press.menu()
                time.sleep(2)
                if d(text="Record FM",className="android.widget.TextView",resourceId="android:id/title").exists:
                    print("Test Record FM")
                    d(text="Record FM",className="android.widget.TextView",resourceId="android:id/title").click()
                    time.sleep(2)
                if d(description="power",className="android.widget.TextView").exists:
                    print("Click Exit Menu")
                    d(description="power",className="android.widget.TextView").click()
                    time.sleep(2)

            else:
                print("Phone need inset earset")
        d.press.back()
        time.sleep(2)


class ContactsTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)


    def test_add_contacts_phone(self):
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)
        print("Add contacts to Phone")
        d(className="android.view.View",resourceId="com.android.launcher3:id/layout").\
            child(description="Apps",className="android.widget.TextView").click()
        time.sleep(2)
        while not d(text="People",className="android.widget.TextView").exists:
            d.drag(240, 360, 5, 360, steps=10)
            time.sleep(2)
        d(text="People",className="android.widget.TextView").click()
        time.sleep(2)

    d.press.back()
    time.sleep(2)
    d.press.back()
    time.sleep(2)
    d.press.home()



class GalleryTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    d.press.back()

    def test_galleryview(self):
        d(className="android.view.View",resourceId="com.android.launcher3:id/layout").\
            child(description="Apps",className="android.widget.TextView").click()
        # d(description="Apps",className="android.widget.TextView").click()
        time.sleep(2)
        if d(text="Gallery",className="android.widget.TextView").exists:
            d(text="Gallery",className="android.widget.TextView").click()
            time.sleep(2)
            if d(text="Camera",className="android.widget.Button").exists:
                print("Not Any picture,will tack some picture")
                d(text="Camera",className="android.widget.Button").click()
                time.sleep(2)
                d(description="Shutter button",className="android.widget.ImageView",resourceId="com.android.gallery3d:id/shutter_button_photo").click()
                time.sleep(5)
                d.press.back()
                time.sleep(2)
            else:
                print("Gallery have some picture,not need photograph")
            d.press.back()
            time.sleep(2)
        else:
            print("No found Gallery APP")
        d.press.home()
        time.sleep(1)

    def test_gallery_menu_delete(self):
        print("Gallery----Menu-----Del")
        d(className="android.view.View",resourceId="com.android.launcher3:id/layout").child(description="Apps",className="android.widget.TextView").click()
        time.sleep(2)



    def test_gallery_menu_rotate(self):
        print("Gallery----Menu----Rotate right/left")

    def test_gallery_menu_slideshow(self):
        print("Gallery----Menu----Slideshow")

    def test_gallery_menu_edit(self):
        print("Gallery----Menu----Edit")

    def test_gallery_menu_set_picture_as(self):
        print("Gallery----Menu----Set picture as")

    def test_gallery_menu_details(self):
        print("Gallery----Menu----Details")



class ClockTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
    d.press.back()

    def testclock_add(self):
        print("add clock")
        d.press.home()
        time.sleep(2)
        d(className="android.view.View",resourceId="com.android.launcher3:id/layout").\
            child(description="Apps",className="android.widget.TextView").click()
        time.sleep(2)
        if d(text="Clock",className="android.widget.TextView").exists:
            d(text="Clock",className="android.widget.TextView").click()
            time.sleep(2)
            d(description="Alarm",className="android.widget.ImageView").click()
            time.sleep(2)
            d(description="Add alarm",className="android.widget.ImageView",resourceId="com.android.deskclock:id/alarm_add_alarm").click()
            time.sleep(2)
            d(text="Done",className="android.widget.Button",resourceId="com.android.deskclock:id/done_button").click()
            time.sleep(2)
            d(description="Delete alarm",className="android.widget.ImageView",resourceId="com.android.deskclock:id/delete").click()
            time.sleep(2)
            d.press.back()
            time.sleep(2)
        else:
            print("No found Clock APP")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)




if __name__ == '__main__':
    unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(IdleScreenTestCase)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(PhoneTestCase)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(MMSTestCase)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(LauncherTestCase)
    suite5 = unittest.TestLoader().loadTestsFromTestCase(CameraTestCase)
    suite6 = unittest.TestLoader().loadTestsFromTestCase(SettingsTestCase)
    suite7 = unittest.TestLoader().loadTestsFromTestCase(EmailTestCase)
    suite8 = unittest.TestLoader().loadTestsFromTestCase(ContactsTestCase)
    suite9 = unittest.TestLoader().loadTestsFromTestCase(GalleryTestCase)
    clock = unittest.TestLoader().loadTestsFromTestCase(ClockTestCase)
    sms = unittest.TestLoader().loadTestsFromTestCase(SMSTestCase)

    suite = unittest.TestSuite([suite1, suite2,suite3,sms,suite4,suite5,suite6,suite7,suite8,suite9,clock])
    unittest.TextTestRunner(verbosity=11).run(suite)