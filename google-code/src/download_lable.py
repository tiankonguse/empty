#!/usr/bin/python
# coding:UTF-8

import MySQLdb
import sys
import re

import os

import urllib
import urllib2
import traceback
import requests

from lxml import etree as ET
import json

import time

import datetime
import logging
import cStringIO
import random
import socks
import socket


import re
from BeautifulSoup import BeautifulSoup 

useragent = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
    'X-Forwarde-For':'127.0.0.1'
}

#field_names = [ i[0] for i in cur.description ]
#d = dict(zip(field_names, list(x)))

PROXY = {
    "ip" : "127.0.0.1",
    "port" : 7070
}


GOOGLE_CODE_DBCFG = {
    "host" : "127.0.0.1",
    "port" : 3306,
    "user" : "google_code",
    "passwd" : "google_code",
    "db" : "d_google_code_backup"
}


SEARCH_LABLE = 'https://code.google.com/hosting/search?q=label:%s&filter=0&mode=&start=%d'


def init(ret):

    reload(sys)
    sys.setdefaultencoding('utf8')

    today = datetime.date.today()
    logfilepath = "../log/" + os.path.splitext(os.path.basename(__file__))[0] + "_" + today.strftime('%Y%m%d') + ".log"
    logging.basicConfig(filename=logfilepath, level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s: %(message)s')

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, PROXY["ip"], PROXY["port"])
    socket.socket = socks.socksocket

#end init


def myrand():
    return random.randint(1, 126)
#end myrand

def rand_ip():
    return ("127.%d.%d.%d`" % (myrand(), myrand(),myrand()))
#rand_ip

def download(info, ret):
    try:
        url = info["url"]
        useragent['X-Forwarde-For'] = rand_ip()
        req = urllib2.Request(url, None, useragent)
        info["content"] = urllib2.urlopen(req).read()
        
    except urllib2.HTTPError, e:
        ret["code"] = -1
        ret["msg"] = ('(%s)http request error code - %s.' % (url, e.code))
    except urllib2.URLError, e:
        ret["code"] = -1
        ret["msg"] = ('(%s)http request error reason - %s.' % (url, e.reason))
    except Exception: 
        ret["code"] = -1
        ret["msg"] = ('(%s)http request generic exception: %s.' % (url, traceback.format_exc()))
#end test


def is_chinese(uchar):
    #判断一个unicode是否是汉字
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

def is_number(uchar):
    #判断一个unicode是否是数字
    if uchar >= u'\u0030' and uchar<=u'\u0039':
        return True
    else:
        return False


def is_alphabet(uchar):
    #判断一个unicode是否是英文字母
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
        return True
    else:
        return False

def is_ascii(uchar):
    #判断一个unicode是否是ascii
    if (uchar >= u'\u0000' and uchar<=u'\u00ef'):
        return True
    else:
        return False
#end is_ascii


def is_fetch_char(uchar):
    if (is_ascii(uchar) or is_chinese(uchar)):
        return True
    else:
        return False
#end is_fetch_char




def readLableInfo(lableInfo, ret):
    try:
        dbcfg = GOOGLE_CODE_DBCFG
        conn = MySQLdb.connect(host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor()
        sql = "SELECT c_id, c_name, c_search_page, c_max_num FROM d_google_code_backup.t_lable where c_max_num = 0 or c_search_page < c_max_num limit 1;"
        cur.execute(sql)
        results = cur.fetchall()
        for x in results:
            lableInfo["id"] = x[0]
            lableInfo["lableName"] = x[1]
            lableInfo["nowNum"] = x[2]
            lableInfo["maxNum"] = x[3]
        
        if lableInfo["id"] == 0:
            ret["code"] = -1
            ret["msg"] = "all searched"
          
        conn.close()
    except MySQLdb.Error, e:
        ret["code"] = -1
        ret["msg"] = ("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error(ret["msg"])
#end fetchMatchState


def getSearchUrl(lableInfo, ret):
    lableInfo["url"] = (SEARCH_LABLE % (lableInfo["lableName"], lableInfo["nowNum"]))
#end getSearchUrl

def fetchPrjList(info, ret):
    prjList = info["prjList"]
    soup = BeautifulSoup(info["content"])
    
    if info["maxNum"] == 0:
        tdList = soup.find(attrs={"class": "mainhdr"}).findAll("td")
        if len(tdList) == 0:
            return
        info["maxNum"] = tdList[1].string.strip().split(' ')[-1]
        info["maxNum"] = int(info["maxNum"])
    
    serp = soup.find(id='serp')
    
    tableList = serp.findAll('table')
    

    
    for table in tableList:
        prj = {
            "prjName" : "",
            "lableList" : []    
        }
        lableList = prj["lableList"]
        
        tdList = table.findAll('td')
        
        prjLink = tdList[0].find('a')["href"]
        
        prj["prjName"] = prjLink[3:-1]
        
        info["nowNum"] = info["nowNum"] + 1
        
        if not is_fetch_char(prj["prjName"]):
            continue
        
        ptjLableLink = tdList[1].find(attrs={"class": "labels"}).findAll("a")
        
        for link in ptjLableLink:
            lableName = link.string
            if not is_fetch_char(lableName):
                continue
            lableList.append(lableName)
        
        prjList.append(prj)
        
#end fetchPrjList


def updateLable(info, ret):
    try:
        dbcfg = GOOGLE_CODE_DBCFG
        conn = MySQLdb.connect(host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor()
        
        id = info["id"]
        nowNum = info["nowNum"]
        maxNum = info["maxNum"]
        
        sql = ("update d_google_code_backup.t_lable set c_search_page = %d , c_max_num = %d where c_id = %d;" % (nowNum, maxNum, id))
        logging.debug(sql)
        cur.execute(sql)
        conn.commit()
        conn.close()
    except MySQLdb.Error, e:
        ret["code"] = -1
        ret["msg"] = ("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error(ret["msg"])
#end updateLable


def savePrj(prj, ret):
    try:
        dbcfg = GOOGLE_CODE_DBCFG
        conn = MySQLdb.connect(host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor()
        
        prjName = prj["prjName"]
        prjName = conn.escape_string(prjName)

        sql = ("SELECT count(*) FROM d_google_code_backup.t_project where c_name = '%s';" % (prjName))
        cur.execute(sql)
        results = cur.fetchall()
        count = 0
        for x in results:
            count = x[0]
        
        if count != 0 :
            return
        
        sql = ("INSERT INTO `d_google_code_backup`.`t_project` (`c_name`, `c_starred_num`, `c_members_num`, `c_ok`) VALUES ('%s', 0, 0, 0);" % (prjName))
        cur.execute(sql)
        logging.debug(sql)
        conn.commit()
        conn.close()
    except MySQLdb.Error, e:
        ret["code"] = -1
        ret["msg"] = ("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error(ret["msg"])
#end savePrj


def connect(lableName, prjName, ret):
    try:
        dbcfg = GOOGLE_CODE_DBCFG
        conn = MySQLdb.connect(host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor()
        
        lableName = conn.escape_string(lableName)
        prjName = conn.escape_string(prjName)
        sql = ("SELECT count(*) FROM d_google_code_backup.t_prj_lable where c_prj_name='%s' and c_lable_name = '%s';" % (prjName, lableName))
        cur.execute(sql)
        results = cur.fetchall()
        count = 0
        for x in results:
            count = x[0]
        
        if count != 0 :
            return
        
        sql = ("INSERT INTO `d_google_code_backup`.`t_prj_lable` (`c_prj_name`, `c_lable_name`) VALUES ('%s', '%s');" % (prjName, lableName))
        cur.execute(sql)
        logging.debug(sql)
        conn.commit()
        conn.close()
    except MySQLdb.Error, e:
        ret["code"] = -1
        ret["msg"] = ("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error(ret["msg"])
#end connect

def saveLable(info, ret):

    lableName = info["lableName"]
    
    prjList = info["prjList"]
    for prj in prjList:
        prjName = prj["prjName"]
        savePrj(prj, ret)
        if ret["code"] != 0:
            print ret
            return
        connect(lableName, prjName, ret)
        if ret["code"] != 0:
            print ret
            return
    
    
    
    updateLable(info, ret)
    
    if ret["code"] != 0:
        print ret
        return
    
        
#end saveData


def run(ret):
    lableInfo = {
        "id" : 0,
        "lableName" : "",
        "nowNum" : 0,
        "maxNum" : 0,
        "url" : "",
        "content" : "",
        "prjList" : []
    }

    
    print "readLableInfo begin ",time.asctime( time.localtime(time.time()) )
    readLableInfo(lableInfo, ret)
        
    if ret["code"] != 0:
        print ret
        return
    
        
    print "getSearchUrl begin ",time.asctime( time.localtime(time.time()) )
    getSearchUrl(lableInfo, ret)
        
    if ret["code"] != 0:
        print ret
        return
        
    print "download begin ",time.asctime( time.localtime(time.time()) )
    download(lableInfo, ret)
        
    if ret["code"] != 0:
        print ret
        return
    
    print "fetchPrjList begin ",time.asctime( time.localtime(time.time()) )
    fetchPrjList(lableInfo, ret)
    
        
    if ret["code"] != 0:
        print ret
        return
    
    print "saveLable begin ",time.asctime( time.localtime(time.time()) )
    saveLable(lableInfo, ret)
        
    if ret["code"] != 0:
        print ret
        return
#end run

def main():
    
    ret = {
        "code" : 0, 
        "msg":"sucess"
    }


    
    print "init begin ",time.asctime( time.localtime(time.time()) )
    init(ret)

    
    if ret["code"] != 0:
        print ret
        return
        
    while True:
        run(ret)
        if ret["code"] != 0:
            print ret
            return
        time.sleep(3)
#end main

if __name__ == "__main__": 
    main()
        
