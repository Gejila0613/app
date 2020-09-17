# -*- coding: utf-8 -*-


from demo4_qu_tiao_try import driver
#id
driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys('小可爱trr')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext")').send_keys('trr123456')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_login_btn")').click()
#name
driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("请输入用户名")').send_keys('小可爱trr')
#class
driver.find_element_by_android_uiautomator\
    ('new UiSelector().className("android.widget.EditText")').send_keys('小可爱trr')