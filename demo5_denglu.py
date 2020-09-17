# -*- coding: utf-8 -*-


from demo4_qu_tiao_try import driver,NoSuchElementException

def denglu():
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('小可爱trr')

    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('trr123456')
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

try:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
except NoSuchElementException:
    denglu()
else:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
    denglu()

