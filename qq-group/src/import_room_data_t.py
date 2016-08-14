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
import thread
import threading
import re
from bs4 import BeautifulSoup
import Queue
import fcntl  
import chardet


useragent = {
    'Host':'qun.col.pw',
    'X-Forwarde-For':'195.154.92.79',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-language' : 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    'Referer' : 'http://qun.col.pw/',
    'cookie': 'CNZZDATA5812234=cnzz_eid%3D763641837-1426399505-http%253A%252F%252Fsite1.sfz.col.pw%252F%26ntime%3D1441550548'
}



PROXY = {
    "ip" : "127.0.0.1",
    "port" : 7070
}


QQ_DBCFG = {
    "host" : "127.0.0.1",
    "port" : 3306,
    "user" : "user_qq",
    "passwd" : "pw_qq",
    "db" : "d_qq"
}

QQ_URL = 'http://195.154.92.79/doquery.php?q=%d&type=1'
GROUP_URL = 'http://195.154.92.79/doquery.php?q=%d&type=2'

HTTP_CODE = [404, 403, 500, 301]
HTTP_CORE_DOWN = [301]

GROUP_ALL_SEARCH = -2
MYSQL_ERROR = -3
QQ_ALL_SEARCH = -4
URL_ERROR = -5
DOWNLOAD_EXCEPTION = -6
HTTP_ERROR = -7
STR_EXCEPTION = -8
ALL_SEARCH = -9

dbcfg = QQ_DBCFG
TABLE_MAX = 10

def Rs_hash(str):
    b = 378551
    a = 63689
    hash = 0
    max_uint = 4294967296
    max_and = 2147483648
    for c in str:
    	hash = hash * a + ord(c)
    	hash %= max_uint
    	a *= b
    	a %= max_uint
    return hash % max_and
# end RS_hash

def init ( ret):
    reload ( sys)
    sys.setdefaultencoding ( 'utf8')

    today = datetime.date.today ( )
    logfilepath = "../log/" + os.path.splitext ( os.path.basename(__file__))[0] + "_" + today.strftime('%Y%m%d') + ".log"
    logging.basicConfig ( filename=logfilepath, level=logging.ERROR, filemode='a', format='%(asctime)s - %(levelname)s: %(message)s')

    #socks.setdefaultproxy ( socks.PROXY_TYPE_SOCKS5, PROXY["ip"], PROXY["port"])
    #socket.socket = socks.socksocket
#end init


def readData(ret, peopleList, ex):
    try:
        f = open("../data/room_again_a%s" % (ex), 'r')
        f_ex = open("../data/room_again_a%s_ex" % (ex), 'w')
        
        nameIndex = 0
        cardTypeIndex = 3
        cardIndex = 4
        sexIndex = 5
        birthdayIndex = 6
        addressIndex = 7
        zipIndex = 8
        mobileIndex = 19
        emailIndex = 22
        versionIndex = 31
        
        lines = f.readlines()
        i = 0
        for line in lines:
            i += 1
            #print i
            line = line.strip() 
            if len(line) == 0:
                continue
            
            #line = line.decode('GBK').encode('utf-8')
            lineData = line.split("\t") 
            #print lineData
            if len(lineData) != 33:
                #print ("error data %s" % line) 
                f_ex.write("%s"%( line))
                #logging.error("error data %s" % line) 
                continue
            
            c_card_type = lineData[cardTypeIndex]
            c_card_id = lineData[cardIndex]
            c_name = lineData[nameIndex]
            c_sex = lineData[sexIndex]
            c_birthday = lineData[birthdayIndex]
            c_address = lineData[addressIndex]
            c_zip = lineData[zipIndex]
            c_mobile = lineData[mobileIndex]
            c_eMail = lineData[emailIndex]
            c_version = lineData[versionIndex]
            
            index = Rs_hash(c_card_id)%TABLE_MAX
            
            try:
                if len(c_card_id):
                    c_card_id = c_card_id.decode('GB18030').encode('utf-8')
                if len(c_card_type):
                    c_card_type = c_card_type.decode('GB18030').encode('utf-8')
                if len(c_name):
                    c_name = c_name.decode('GB18030').encode('utf-8')
                if len(c_sex):
                    c_sex = c_sex.decode('GB18030').encode('utf-8')
                if len(c_birthday):
                    c_birthday = c_birthday.decode('GB18030').encode('utf-8')
                if len(c_mobile):
                    c_mobile = c_mobile.decode('GB18030').encode('utf-8')
                if len(c_eMail):
                    c_eMail = c_eMail.decode('GB18030').encode('utf-8')
                if len(c_address):
                    c_address = c_address.decode('GB18030').encode('utf-8')
                if len(c_zip):
                    c_zip = c_zip.decode('GB18030').encode('utf-8')
                if len(c_version):
                    c_version = c_version.decode('GB18030').encode('utf-8')

            except UnicodeDecodeError:
                #logging.error("decode error: line=%d c_name=%s", i, c_name)
                f_ex.write("%s"%(line))
                continue
            
            
            obj = {
                "c_card_id" : c_card_id,
                "c_card_type" : c_card_type,
                "c_name" : c_name,
                "c_sex" : c_sex,
                "c_birthday" : c_birthday,
                "c_mobile" : c_mobile,
                "c_eMail" : c_eMail,
                "c_address" : c_address,
                "c_zip" : c_zip,
                "c_version" : c_version,
            }
            peopleList[index].append(obj)
            #print obj
            #if i > 10 :
            #    break
            
            #print peopleList
            #ret["code"] = 2
            #return
            
        f_ex.close()
        f.close()
    except IOError, e:
        logging.error("Error %d: %s" % (e.args[0], e.args[1]))
        ret["code"] = 2
#end readData

def runRoom(index, peopleList):
    try:
        dbcfg = QQ_DBCFG
        conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor ( )
        
        for people in peopleList:
        
            c_card_id = conn.escape_string(people["c_card_id"])
            c_name = conn.escape_string(people["c_name"])
            c_sex = conn.escape_string(people["c_sex"])
            c_address = conn.escape_string(people["c_address"])
            c_mobile = conn.escape_string(people["c_mobile"])
            c_eMail = conn.escape_string(people["c_eMail"])
            c_card_type = conn.escape_string(people["c_card_type"])
            c_birthday = conn.escape_string(people["c_birthday"])
            c_zip = conn.escape_string(people["c_zip"])
            c_version = conn.escape_string(people["c_version"])
            
            
            sql = ( "SELECT c_card_id FROM d_qq.t_people_info_%d where c_card_id='%s' limit 1" % (index, c_card_id))
            cur.execute ( sql)
            results = cur.fetchall ( )
            count = 0
            for x in results:
                count = 1
                
            if count == 0:
                sql = ( "INSERT INTO t_people_info_%d (c_card_id,c_name,c_sex,c_address,c_mobile,c_eMail,c_card_type,c_birthday,c_zip,c_version) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (index, c_card_id, c_name, c_sex, c_address, c_mobile,c_eMail,c_card_type,c_birthday,c_zip,c_version))
                logging.info(sql)
                cur.execute ( sql)
                conn.commit ( )
        conn.close ( )
    except MySQLdb.Error, e:
        #ret["code"] = MYSQL_ERROR
        msg = ( "Mysql Error %d: %s sql:%s" % (e.args[0], e.args[1],sql))
        logging.error (msg)
#end updateQQ


def runHelp(ret, peopleList):
    print "runHelp"
    
    threads = []

    index = 0
    while index < TABLE_MAX:
        print index, len(peopleList[index])
        threads.append(threading.Thread(target=runRoom, args=(index, peopleList[index])))
        index = index + 1
        
    
    # 启动所有线程
    for t in threads:
        t.start()
        
    # 主线程中等待所有子线程退出
    for t in threads:
        t.join() 
   
#end runQQHelp

def mainHelp(ex):
    ret = {
        "code" : 0,
        "msg":"sucess"
    }
    
    peopleList = []
    
    index = 0
    while index < TABLE_MAX:
        peopleList.append([])
        index = index + 1
    
    
    readData(ret, peopleList, ex)
    if ret["code"] != 0:
        print ret
        return
    
    #print peopleList
    runHelp(ret, peopleList)
    
#end mainHelp


def main ():
    
    print "init begin ",time.asctime ( time.localtime(time.time()) )

    ret = {
        "code" : 0,
        "msg":"sucess"
    }
    init ( ret)

    threads = []

    begin = ord('t')
    end = ord('t')
    while begin <= end:
        print begin, chr(begin)
        mainHelp(chr(begin))
        #threads.append(threading.Thread(target=mainHelp, args=(chr(begin))))
        begin += 1
        
    # 启动所有线程
    for t in threads:
        t.start()
        time.sleep (20)
        
    # 主线程中等待所有子线程退出
    for t in threads:
        t.join() 
#end main


def lockFile(lockfile):  
    fp = os.open(lockfile, os.O_CREAT | os.O_TRUNC | os.O_WRONLY)
    try:  
        fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)  
        print ("lockFile ok ")
    except IOError, e:
        print ("lockFile error %d=s %s" % (e.args[0], e.args[1]))
        return False  
    return True 
    
if __name__ == "__main__":
    if not lockFile("import_room_data_t.lock.pid"):  
        sys.exit(0) 
    main()


