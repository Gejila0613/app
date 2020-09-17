# -*- coding: utf-8 -*-


import unittest
from demo27_qidongpeizhi import app_qidongpeizhi
import logging
from  time import sleep

class kaishijieshu(unittest.TestCase):

    def setUp(self):
        logging.info('======开始setUp=========')
        self.driver=app_qidongpeizhi()


    def tearDown(self):
        logging.info('======结束tearDown=====')
        sleep(5)
        self.driver.close_app()
