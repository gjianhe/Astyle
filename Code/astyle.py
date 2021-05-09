#! python3
# -*- coding: utf-8 -*-

__author__ = 'guanjianhe'

import sys
import os
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')



def astyle(filename):
    s = "C:\\\"Program Files (x86)\"\\Dev-Cpp\\AStyle\\AStyle.exe --options=\"C:\\Program Files (x86)\\Dev-Cpp\\AStyle\\AS.cfg\" "
    os.system(s+filename)




if __name__ == '__main__':

    logging.info("author:guanjianhe")
    logging.info("version:1.00")
    logging.info("update:2021-05-08")
    logging.info("程序开始执行中……")

    filelists = []
    basedir = os.getcwd()
    whitelist = ['c', 'h']

    for parent, dirnames, filenames in os.walk(basedir):
        for filename in filenames:
            ext = filename.split('.')[-1]
            if ext in whitelist:
                filelists.append(os.path.join(parent, filename))

    if len(filelists):
        logging.info("找到文件!")
        for file in filelists:
            logging.info(os.path.basename(file))
    else:
        logging.error('没有找到文件，请检查该目录下是否有.c or .h文件')
        input('按回车键退出')
        sys.exit()

    for filelist in filelists:
        astyle(filelist)

    logging.info('程序执行完成')
    input('按回车键退出')
    sys.exit()
