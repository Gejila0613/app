# -*- coding: utf-8 -*-
# @Author ：大汉老师
# @Software：测码学院
# @Email:896096254@qq.com


from demo4_qu_tiao_try import driver

driver.find_element_by_class_name('android.widget.EditText').send_keys('小可爱trr')
driver.find_element_by_class_name('android.widget.EditText').send_keys('trr123456')

#list
#driver.find_elements_by_class_name('android.widget.EditText')[0].send_keys('小可爱trr')
#driver.find_elements_by_class_name('android.widget.EditText')[1].send_keys('trr123456')