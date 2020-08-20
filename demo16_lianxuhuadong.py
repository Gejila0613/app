# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from appium import webdriver
from  time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


cunchuxinxi={}
cunchuxinxi['platformName']='Android'
cunchuxinxi['platformVersion']='5.1.1'
cunchuxinxi['deviceName']='127.0.0.1:62001'

cunchuxinxi['app']=r'C:\Users\m1877\Desktop\mymoney.apk'
cunchuxinxi['appPackage']='com.mymoney'
cunchuxinxi['appActivity']='com.mymoney.biz.splash.SplashScreenActivity'
cunchuxinxi['noReset']='False'

driver = webdriver.Remote('http://localhost:4723/wd/hub', cunchuxinxi)
driver.implicitly_wait(5)

def chicun():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y

def swipeLeft():
    l=chicun()
    x1=int(l[0]*0.9)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)

def swipeUp():
    l = chicun()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.95)
    y2 = int(l[1] * 0.35)
    driver.swipe(x1, y1, x1, y2, 1000)

WebDriverWait(driver,6).until(lambda x:x.find_element_by_id("com.mymoney:id/next_btn"))
for i in range(2):
    swipeLeft()
    sleep(1)
#点击随手记
driver.find_element_by_id('com.mymoney:id/begin_btn').click()

try:
    closBtn=driver.find_element_by_id('com.mymoney:id/close_iv')
except NoSuchElementException:
    pass
else:
    closBtn.click()

driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()

WebDriverWait(driver,6).until(lambda x:x.find_element_by_id("com.mymoney:id/content_container_ly"))
swipeUp()

driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()

driver.find_element_by_id('com.mymoney:id/password_protected_briv').click()

driver.find_element_by_id('com.mymoney:id/lock_pattern_or_not_sriv').click()

for i in range(2):
    TouchAction(driver).press(x=246,y=376).wait(2000)\
        .move_to(x=451,y=385).wait(1000)\
        .move_to(x=644,y=584).wait(1000)\
        .move_to(x=661,y=774).wait(1000)\
        .release().perform()
