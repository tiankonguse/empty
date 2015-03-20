#!/usr/local/services/python/bin/python
# coding:UTF-8

#!/usr/bin/python

import MySQLdb
import sys
import re

import os

import urllib
import urllib2
import traceback


from lxml import etree as ET

import json

import time

import datetime
import logging
import cStringIO
import random

 
debug = 1
prj_id = "5";

reload(sys)

sys.setdefaultencoding('utf8')

today = datetime.date.today()

logfilepath = "../log/" + os.path.splitext(os.path.basename(__file__))[0] + "_" + today.strftime('%Y%m%d') + ".log"

logging.basicConfig(filename=logfilepath, level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s: %(message)s')



useragent = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}



def fetchAccoutInfoList(accoutInfoList):
    filePath = ""
    try:
        if not os.path.exists(filePath):
            stateRet["ret"] = 1
            stateRet["msg"] = ("Error file %s not exit" % (filePath))
            
            print stateRet["msg"] 
            logging.error(stateRet["msg"])
            return 
        f = open(filePath, 'r')
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                continue
            
            #data = line.split('\t')
            #item = x[0].decode("utf8")
            #data = json.loads(line)
            #photos.append({"thumb":thumb, "image":image, "size":size})
        f.close()
    except IOError, e:
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        logging.error("Error %d: %s" % (e.args[0], e.args[1]))
#end fetchYoukuTask

def saveAccointInfo(accoutInfoList):
    try:
        dbcfg=match_dbcfg
        conn = MySQLdb.connect(host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor()
        sql = "SELECT c_acount_name, c_from, c_vplus_account,c_acount_url,c_all_play_num,c_fans_num,c_video_num FROM d_v_idx.t_cp_info;"
        cur.execute(sql)
        results = cur.fetchall()
        for x in results:
            item = x[0].decode("utf8")
            
            # sql = ("SELECT c_id FROM d_v_idx.t_cp_info where c_acount_name ='%s' limit 1;" % (conn.escape_string(youkuname)))
                
        conn.close()
    except MySQLdb.Error, e:
        logging.error("Mysql Error %d: %s" % (e.args[0], e.args[1]))
#end fetchMatchState


def main():
    accoutInfoList = []
    
    
    print "fetchAccoutInfoList begin ",time.asctime( time.localtime(time.time()) )
    fetchAccoutInfoList(accoutInfoList)
    print "accoutInfoList size=",len(accoutInfoList)
    
    
    print "fetchVPlusData begin ",time.asctime( time.localtime(time.time()) )
    saveAccointInfo(accoutInfoList)
    
    print "end ",time.asctime( time.localtime(time.time()) )
    
if __name__ == "__main__": 
    main()

