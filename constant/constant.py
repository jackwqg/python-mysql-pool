#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import os
from  util.logger import  *

reload(sys)
sys.setdefaultencoding('utf-8')

currentPath = os.path.split(os.path.realpath(__file__))[0]
loggingerr=currentPath+'/../log/logging.err'


# MAIN
# ===============================================
if __name__ == '__main__':
    logging.info('main starts...')
    print  loggingerr
    logging.info('main stop')
    sys.exit(0)