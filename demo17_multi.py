# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


cunchuxinxi={}
cunchuxinxi['platformName']='Android'
cunchuxinxi['deviceName']='127.0.0.1:62025'
cunchuxinxi['platforVersion']='5.1.1'

cunchuxinxi['app']=r'C:\Users\m1877\Desktop\com.baidu.BaiduMap.apk'
cunchuxinxi['appPackage']='com.baidu.BaiduMap'
cunchuxinxi['appActivity']='com.baidu.baidumaps.WelcomeScreen'

driver=webdriver.Remote('http://localhost:4723/wd/hub',cunchuxinxi)
driver.implicitly_wait(5)

#driver.find_element_by_id('com.baidu.BaiduMap:id/dj2').click()
driver.find_element_by_id('com.baidu.BaiduMap:id/ai5').click()

x=driver.get_window_size()['width']
y=driver.get_window_size()['height']

def pinch():
    action1=TouchAction(driver)
    action2=TouchAction(driver)
    zoom_action=MultiAction(driver)

#缩小地图
    action1.press(x=x*0.2,y=y*0.2).wait(1000).move_to(x=x*0.4,y=y*0.4).wait(1000).release()
    action2.press(x=x*0.8,y=y*0.8).wait(1000).move_to(x=x*0.6,y=y*0.6).wait(1000).release()

    print('start pinch...')
    zoom_action.add(action1,action2)
    zoom_action.perform()

def zoom():
    action1=TouchAction(driver)
    action2=TouchAction(driver)
    zoom_action=MultiAction(driver)

#放大地图
    action1.press(x=x*0.4,y=y*0.4).wait(1000).move_to(x=x*0.2,y=y*0.2).wait(1000).release()
    action2.press(x=x*0.6,y=y*0.6).wait(1000).move_to(x=x*0.8,y=y*0.8).wait(1000).release()

    print('start zoom...')
    zoom_action.add(action1,action2)
    zoom_action.perform()

if __name__ == '__main__':
    for i in range(3):
        pinch()

    for i in range(3):
        zoom()