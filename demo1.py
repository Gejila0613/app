# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from appium import webdriver

#定义一个字典去存储信息
cunchuxinxi={}
cunchuxinxi['platformName']='Android'
#模拟器
cunchuxinxi['platformVersion']='5.1.1'
cunchuxinxi['deviceName']='127.0.0.1:62001'

#真机
# cunchuxinxi['platformVersion']='5.1.1'
# cunchuxinxi['deviceName']='设备名'
# cunchuxinxi['udid']='手机usb连接的串码'

cunchuxinxi['app']=r'C:\Users\m1877\Desktop\kaoyan3.1.0.apk'
cunchuxinxi['appPackage']='com.tal.kaoyan'
cunchuxinxi['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

driver=webdriver.Remote('http://localhost:4723/wd/hub',cunchuxinxi)