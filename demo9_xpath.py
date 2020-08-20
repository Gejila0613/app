# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com

from demo4_qu_tiao_try import driver

driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名"]').send_keys('小可爱trr')
#*匹配所有节点，光用class是不行的，有很多重复的，所以用到组合定位
driver.find_element_by_xpath('//*[@class="android.widget.EditText" and @index="3"]').send_keys('trr123456')

driver.find_element_by_xpath('//android.widget.Button').click()

# driver.find_element_by_xpath('//*[@class="android.widget.Button"]').click()