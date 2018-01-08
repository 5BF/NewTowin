from selenium import webdriver
#登录模块
def login(self,username,password):
    driver=self.driver
    driver.find_element_by_id("account").clear()
    driver.find_element_by_id("account").send_keys(username)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath("//*[@id='loginForm']/div/div/div/button").click()


def logout(self):
    driver=self.driver
    driver.find_element_by_xpath("//*[@id='loginedSpan']/a[2]").click()


