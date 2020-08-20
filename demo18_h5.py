# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from  appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

cunchuxinxi={}
cunchuxinxi['platformName']='Android'
cunchuxinxi['platformVersion']='5.1.1'
cunchuxinxi['deviceName']='127.0.0.1:62001'

cunchuxinxi['app']=r'C:\Users\m1877\Desktop\dr.fone3.2.0.apk'
cunchuxinxi['appPackage']='com.wondershare.drfone'
cunchuxinxi['appActivity']='com.wondershare.drfone.ui.activity.WelcomeActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', cunchuxinxi)
driver.implicitly_wait(5)

print('点击backup按钮1')
driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()
print('点击backup完成2')
WebDriverWait(driver,20).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))

print('点击next按钮3')
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()
print('点击next完成4')

contexts=driver.contexts
print(contexts)
print('获取contexts完成5')

print('开始切换进内嵌网页6')
driver.implicitly_wait(10)
driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
print('已经切换到内嵌网页7')

driver.find_element_by_id('email').send_keys('123@wondershare.cn')

print('页面操作完成，准备开始跳出h5页面8')
#切换context 点击返回
#driver.switch_to.context(contexts[0])
driver._switch_to.context('NATIVE_APP')
print('跳出h5，返回app，完成 9')