# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from  appium import webdriver

cunchuxinxi={}
cunchuxinxi['platformName']='Android'
cunchuxinxi['deviceName']='127.0.0.1:62025'
cunchuxinxi['platforVersion']='5.1.1'


cunchuxinxi['app']=r'C:\Users\m1877\Desktop\kaoyan3.1.0.apk'
cunchuxinxi['appPackage']='com.tal.kaoyan'
cunchuxinxi['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'
#非首次启动时保留上次操作true。默认是false（重新安装）
cunchuxinxi['noReset']='True'

driver=webdriver.Remote('http://localhost:4723/wd/hub',cunchuxinxi)
driver.implicitly_wait(5)


#取消按钮（先定义一个存储取消升级的变量）
quxiaoanniu=driver.find_element_by_id('android:id/button2')
#点击跳过（在定义一个跳过按钮的变量，先把他存储起来不去点击）
tiaoguoanniu=driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')

if quxiaoanniu:
    quxiaoanniu.click()
else:
    print('没有取消按钮')


if tiaoguoanniu:
    tiaoguoanniu.click()
else:
    print('没有跳过按钮')

#在配置文件中写cunchuxinxi['noReset']='True'