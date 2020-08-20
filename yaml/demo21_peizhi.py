# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from appium import webdriver
import yaml

file=open('demo20_canshupeizhi.yaml','r')
#data=yaml.load(file)
data=yaml.load(file,Loader=yaml.FullLoader)

cunchuxinxi={}
cunchuxinxi['platformName']=data['platformName']

cunchuxinxi['platformVersion']=data['platformVersion']
cunchuxinxi['deviceName']=data['deviceName']

cunchuxinxi['app']=data['app']
cunchuxinxi['noReset']=data['noReset']

cunchuxinxi['appPackage']=data['appPackage']
cunchuxinxi['appActivity']=data['appActivity']

driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', cunchuxinxi)



