# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from  appium import webdriver
from selenium.common.exceptions import NoSuchElementException

cunchuxinxi={}
cunchuxinxi['platformName']='Android'
cunchuxinxi['deviceName']='127.0.0.1:62025'
cunchuxinxi['platforVersion']='5.1.1'
# cunchuxinxi['automationName']='uiautomator2'

cunchuxinxi['app']=r'C:\Users\m1877\Desktop\kaoyan3.1.0.apk'
cunchuxinxi['appPackage']='com.tal.kaoyan'
cunchuxinxi['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

cunchuxinxi['noReset']='False'
cunchuxinxi['unicodeKeyboard']='True'
cunchuxinxi['resetKeyboard']='True'

driver=webdriver.Remote('http://localhost:4723/wd/hub',cunchuxinxi)
driver.implicitly_wait(5)

#
def jiancha_quxiao():
    print("开始检查是否有取消")

    try:
        quxiaoanniu = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('没有取消按钮')
    else:
        quxiaoanniu.click()


def jiancha_tiaoguo():
    print("开始检查是否有跳过")
    try:
        tiaoguoanniu = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print("没有跳过")
    else:
        tiaoguoanniu.click()

#最后去调用这两个方法
jiancha_quxiao()
# jiancha_tiaoguo()