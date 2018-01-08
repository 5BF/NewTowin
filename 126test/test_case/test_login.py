from selenium import webdriver
import unittest
from pubile import login
import xml.dom.minidom
import time



print ("GG")
dom=xml.dom.minidom.parse('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\126test\\test_date\\login_data.xml')
root=dom.documentElement

testaaa=root.getElementsByTagName('explain')
GG=testaaa[0].firstChild.data
print(GG)
print ("123")
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        logins=root.getElementsByTagName('url')
        self.base_url=logins[0].firstChild.data
        #self.base_url="http://www.51towin.com"
        print("456")


    #账号一登录
    def test_login(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("login").click()
        account=root.getElementsByTagName('account1')
        username=account[0].getAttribute("username")
        password=account[0].getAttribute("password")
        login.login(self,username,password)
        #login.login(self,"13726245005","123456")
        text=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/p[2]/a[1]").text
        self.assertEqual(text,"吴宝丰")
        self.driver.implicitly_wait(5)
        login.logout(self)
        print("789")



    def test_login2(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("login").click()
        account=root.getElementsByTagName('account2')
        username=account[0].getAttribute("username")
        password=account[0].getAttribute("password")
        login.login(self,username,password)
        text=driver.find_element_by_xpath("//*[@id='loginVaildTips']").text
        self.assertEqual(text, "手机号码未注册用户!")
        print("1011")

    if __name__=="__main__":
        unittest.main()
        print("12")


