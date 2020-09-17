# -*- coding: utf-8 -*-


from demo28_jilei import jilei
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from demo27_qidongpeizhi import app_qidongpeizhi

class gonggong(jilei):

    quxiaoanniu=(By.ID,'android:id/button2')
    tiaoguoanniu=(By.ID,'com.tal.kaoyan:id/tv_skip')

    def jiancha_quxiao(self):
        logging.info("============开始检查取消按钮===============")

        try:
            quxiaoanniu = self.driver.find_element(*self.quxiaoanniu)
        except NoSuchElementException:
            logging.info('取消按钮没有找到')
        else:
            logging.info('点击取消')
            quxiaoanniu.click()

    def jiancha_tiaoguo(self):
        logging.info("==========开始检查跳过按钮===========")
        try:
            tiaoguoanniu = self.driver.find_element(*self.tiaoguoanniu)
        except NoSuchElementException:
            logging.info('跳过按钮没有找到')
        else:
            logging.info('点击跳过')
            tiaoguoanniu.click()

if __name__ == '__main__':

    driver=app_qidongpeizhi()
    com=gonggong(driver)
    com.jiancha_quxiao()
    com.jiancha_tiaoguo()