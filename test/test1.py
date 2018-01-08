from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time
import os
import csv



driver=webdriver.Firefox()
#driver.maximize_window()
driver.get('http://www.51towin.com/0755')
driver.maximize_window()
driver.find_element_by_id('condition').send_keys('688')
driver.find_element_by_xpath("/html/body/div[2]/div[3]/span").click()
driver.refresh()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('宽宽吃鸡')
driver.find_element_by_id('kw').submit()

'''driver.get('http://www.51towin.com/0755')
move_to_element=driver.find_element_by_xpath("/html/body/div[2]/div[4]/span")
ActionChains(driver).move_to_element(move_to_element).perform()

driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/a[1]").click()

title=driver.title
print(title)
now_url=driver.current_url
print(now_url)
driver.find_element_by_id('account').clear()
driver.find_element_by_id('account').send_keys("17666142688")
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys("123456")
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div/div/button').click()

#显示等待，只有检查通过才继续执行
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"condition")))

#隐示等待，到设置的时间后有异常则抛出异常
driver.implicitly_wait(10)
title=driver.title
print(title)
now_url=driver.current_url
print(now_url)
name=driver.find_element_by_xpath('//*[@id="loginedSpan"]/a[1]').text
print(name)'''
'''driver.quit()'''


#frame内
'''file_path=('file:///'+os.path.abspath('test11.10.html'))
driver.get(file_path)

driver.switch_to_frame("if")

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

driver.switch_to_default_content()

driver.find_element_by_id('AAA').send_keys("aaaa")
driver.find_element_by_id('BBB').click()'''

#窗口跳转
'''driver.get("http://www.baidu.com")
sreach_windows=driver.current_window_handle

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[7]").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div/div/div[1]/form/p[9]/a[1]').click()

all_handles=driver.window_handles

for handle in all_handles:
    if handle !=sreach_windows:
        driver.switch_to_window(handle)
        driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_3__userName']").send_keys("这是用户名a")
        driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_3__phone']").send_keys("13726245005")

for  handle in all_handles:
    if handle==sreach_windows:
        driver.switch_to_window(handle)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/a[7]").click()
        driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("Feng_5BF")
        driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("woshigb213")
        driver.find_element_by_id("TANGRAM__PSP_10__submit").click() '''

#滚动条
'''driver.get("http://www.baidu.com")
#driver.set_window_size(500,500)  发现设置了固定大小，滚动条就失效

driver.find_element_by_id("kw").send_keys("NBA")
driver.find_element_by_id("su").click()
time.sleep(3)

js='document.documentElement.scrollTop=10000;'
driver.execute_script(js)
time.sleep(3)

js_="document.documentElement.scrollTop=0;"
driver.execute_script(js_)
time.sleep(3)'''

'''try:               #使用try except 验证，顺带截图
    driver.find_element_by_id("kwaaa").send_keys("NBA")
    driver.find_element_by_id("su").click()
except:
    driver.get_screenshot_as_file("D:\\ceshi.jpg")
    print("错误")'''


#数据驱动登录
'''driver.get("http://www.51towin.com")
driver.find_element_by_link_text("登录").click()
driver.implicitly_wait(10)

class Account(object):
    def __init__(self,username='',password=''):
        self.username=username
        self.password=password

def login(login_info):
    driver.find_element_by_id("account").clear()
    driver.find_element_by_id("account").send_keys(login_info.username)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(login_info.password)
    driver.find_element_by_xpath("/html/body/form/div/div/div/button").click()

admin=Account(username='17666142688',password='123456')

login(admin)'''


#通过文件读取数据
'''driver.get("http://www.51towin.com")
driver.find_element_by_link_text("登录").click()

file_info=open('username.txt','r')
names=file_info.readlines()
file_info.close()

file_info2=open("password.txt",'r')
words=file_info2.readlines()
file_info2.close()

for name in names:
    for word in words:
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys(name)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(word)'''



#使用split截取txt文档中的两个数据
'''driver.get("http://www.51towin.com")
driver.find_element_by_link_text("登录").click()

open_info=open('user.txt','r')
users=open_info.readlines()
open_info.close()

for user in users:
    username=user.split(',')[0]
    password=user.split(',')[1]
    driver.find_element_by_id("account").clear()
    driver.find_element_by_id("account").send_keys(username)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(password)'''


'''my_file='test1.csv'
date=csv.reader(file(my_file,'rb'))
for user in date:
    user1=user[1]
    print(user1)'''









































































