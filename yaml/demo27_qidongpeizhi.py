# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

import yaml
import logging.config
from appium import webdriver


CON_LOG='../runlog/demo24_log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def app_qidongpeizhi():

    stream=open('../yaml/demo20_canshupeizhi.yaml','r')
    data=yaml.load(stream,Loader=yaml.FullLoader)

    cunchuxinxi={}
    cunchuxinxi['platformName']=data['platformName']

    cunchuxinxi['platformVersion']=data['platformVersion']
    cunchuxinxi['deviceName']=data['deviceName']

    cunchuxinxi['app']=data['app']
    cunchuxinxi['noReset']=data['noReset']

    cunchuxinxi['unicodeKeyboard']=data['unicodeKeyboard']
    cunchuxinxi['resetKeyboard']=data['resetKeyboard']

    cunchuxinxi['appPackage']=data['appPackage']
    cunchuxinxi['appActivity']=data['appActivity']
    stream.close()
    logging.info('开始跑app')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', cunchuxinxi)

    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    app_qidongpeizhi()