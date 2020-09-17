# -*- coding: utf-8 -*-


from appium import webdriver
import yaml
from selenium.common.exceptions import NoSuchElementException
import logging

file=open('../yaml/demo20_canshupeizhi.yaml','r')
data=yaml.load(file,Loader=yaml.FullLoader)

logging.basicConfig(level=logging.INFO,filename='../runlog/runlog.log',
                    format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')

cunchuxinxi={}
cunchuxinxi['platformName']=data['platformName']
cunchuxinxi['platformVersion']=data['platformVersion']
cunchuxinxi['deviceName']=data['deviceName']

cunchuxinxi['app']=data['app']
cunchuxinxi['appPackage']=data['appPackage']
cunchuxinxi['appActivity']=data['appActivity']
cunchuxinxi['noReset']=data['noReset']

logging.info('start app...')
driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',cunchuxinxi)

def jiancha_quxiao():
    logging.info("开始检查是否有取消")

    try:
        quxiaoanniu = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        logging.info("没有取消")
    else:
        quxiaoanniu.click()


def jiancha_tiaoguo():
    logging.info("开始检查是否有跳过")

    try:
        tiaoguoanniu = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        logging.info("没有跳过")
    else:
        tiaoguoanniu.click()

jiancha_quxiao()
jiancha_tiaoguo()