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

dbcfg = QQ_DBCFG
conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')

qqSet = set()
groupSet = set()

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

def download ( info, ret):
    try:
        url = info["url"]
        req = urllib2.Request ( url, None, useragent)
        info["content"] = urllib2.urlopen ( req,  timeout=3).read()

    except urllib2.HTTPError, e:
        ret["code"] = HTTP_ERROR
        ret["msg"] = ( '(%s)http request error code - %s.' % (url, e.code))
        if e.code in HTTP_CODE:
            ret["code"] = e.code
    except urllib2.URLError, e:
        ret["code"] = URL_ERROR
        ret["msg"] = ( '(%s)http request error reason - %s.' % (url, e.reason))
    except Exception:
        ret["code"] = DOWNLOAD_EXCEPTION
        ret["msg"] = ( '(%s)http request generic exception: %s.' % (url, traceback.format_exc()))
#end test


def updateQQ(info, ret, conn):
    try:
        
        qq = info["qq"]
        index = Rs_hash(str(qq)) % 10
        cur = conn.cursor ( )

        qqState = info["qqState"]
        
        sql = ( "SELECT c_qq FROM t_qq_info_%d where c_qq=%d limit 1;" % (index, qq))
        cur.execute ( sql)
        results = cur.fetchall ( )
        count = 0
        for x in results:
            count = 1

        #当搜索的是QQ时, state是1, 否则搜索的是group
        sql = ""
        if count == 0 :
            sql = ( "INSERT INTO t_qq_info_%d (c_qq, c_state) VALUES (%d, %d)" % (index, qq, qqState))
        else:
            if qqState:
                sql = ( "UPDATE t_qq_info_%d SET c_state=%d WHERE c_qq=%d" % (index, qqState, qq))
        if len(sql):
            logging.info(sql)
            cur.execute ( sql)
            conn.commit ( )
        #conn.close ( )
    except MySQLdb.Error, e:
        ret["code"] = MYSQL_ERROR
        ret["msg"] = ( "Mysql Error %d: %s sql:%s" % (e.args[0], e.args[1]),sql)
        logging.error ( ret["msg"])
#end updateQQ



def updateGroup(info, ret, conn):
    try:
        
        group = info["group"]
        
        index = Rs_hash(str(group)) % 10
        cur = conn.cursor ( )

        groupState = info["groupState"]
        name = info["name"].strip()

        sql = ( "SELECT c_group FROM t_group_info_%d where c_group=%d limit 1" % (index, group))
        cur.execute ( sql)
        results = cur.fetchall ( )
        count = 0
        for x in results:
            count = 1

        sql = ""
        if count == 0 :
            name = conn.escape_string(name)
            sql = ( "INSERT INTO t_group_info_%d (c_group, c_state, c_group_name) VALUES (%d, %d, '%s')" % (index, group, groupState, name))
        else:
            if groupState :
                if len(name):
                    name = conn.escape_string(name)
                    sql = ( "UPDATE t_group_info_%d SET c_state=%d,c_group_name='%s' WHERE c_group=%d" % (index, groupState, name, group))
                else:
                    sql = ( "UPDATE t_group_info_%d SET c_state=%d WHERE c_group=%d" % (index, groupState, group))

        if len(sql):
            logging.info(sql)
            cur.execute ( sql)
            conn.commit ( )
        #conn.close ( )
    except MySQLdb.Error, e:
        ret["code"] = MYSQL_ERROR
        ret["msg"] = ( "Mysql Error %d: %s sql:%s" % (e.args[0], e.args[1]),sql)
        logging.error ( ret["msg"])
#end updateGroup

def updateQQToGroup(info, ret, conn):
    try:
        cur = conn.cursor ( )

        qq = info["qq"]
        group = info["group"]
        nick = info["nick"].strip()
        role = info["role"].strip()
        sex = info["sex"].strip()
        index = Rs_hash(str(qq)) % 10

        sql = ( "SELECT c_qq FROM t_qq_to_group_%d where c_qq=%d and c_group=%d limit 1" % (index, qq, group))
        cur.execute ( sql)
        results = cur.fetchall ( )
        count = 0
        for x in results:
            count = 1

        sql = ""
        if count == 0 :
            nick = conn.escape_string(nick)
            role = conn.escape_string(role)
            sex = conn.escape_string(sex)
            sql = ( "INSERT INTO t_qq_to_group_%d (c_qq,c_group,c_group_nick,c_group_role,c_group_sex) VALUES (%d, %d, '%s', '%s', '%s');" % (index, qq, group, nick, role ,sex))
            
        if len(sql):
            logging.info(sql)
            cur.execute ( sql)
            conn.commit ( )
        #conn.close ( )
    except MySQLdb.Error, e:
        ret["code"] = MYSQL_ERROR
        ret["msg"] = ( "Mysql Error %d: %s sql:%s" % (e.args[0], e.args[1]),sql)
        logging.error ( ret["msg"])
#end updateQQToGroup

def updateGroupToQQ(info, ret, conn):
    try:
        cur = conn.cursor ( )

        qq = info["qq"]
        group = info["group"]
        nick = info["nick"].strip()
        role = info["role"].strip()
        sex = info["sex"].strip()
        index = Rs_hash(str(group)) % 10

        sql = ( "SELECT c_qq FROM t_group_to_qq_%d where c_qq=%d and c_group=%d limit 1" % (index, qq, group))
        cur.execute ( sql)
        results = cur.fetchall ( )
        count = 0
        for x in results:
            count = 1

        sql = ""
        if count == 0 :
            nick = conn.escape_string(nick)
            role = conn.escape_string(role)
            sex = conn.escape_string(sex)
            sql = ( "INSERT INTO t_group_to_qq_%d (c_qq,c_group,c_group_nick,c_group_role,c_group_sex) VALUES (%d, %d, '%s', '%s', '%s');" % (index, qq, group, nick, role ,sex))
            
        if len(sql):
            logging.info(sql)
            cur.execute ( sql)
            conn.commit ( )
        #conn.close ( )
    except MySQLdb.Error, e:
        ret["code"] = MYSQL_ERROR
        ret["msg"] = ( "Mysql Error %d: %s sql:%s" % (e.args[0], e.args[1]),sql)
        logging.error ( ret["msg"])
#end updateGroupToQQ

def updateMap(info, ret, conn):
    updateQQToGroup(info, ret, conn)
    updateGroupToQQ(info, ret, conn)
#end updateMap

def runQQ(ret, index, conn):
    info = {
        "qq" : 0,
        "qqState" : 1,
        "groupList" : [],
        "url" : "",
        "content" : ""
    }
    
    def readInfo ():
        try:
            cur = conn.cursor ( )
            sql = "SELECT c_qq FROM t_qq_info_%d where c_state = 0 limit 1" % (index)
            cur.execute ( sql)
            results = cur.fetchall ( )
            
            field_names = [ i[0] for i in cur.description ]
            for x in results:
                d = dict ( zip(field_names, list(x)))
                info["qq"] = d["c_qq"]

            if info["qq"] == 0:
                ret["code"] = QQ_ALL_SEARCH
                ret["msg"] = "all searched"

        except MySQLdb.Error, e:
            ret["code"] = MYSQL_ERROR
            ret["msg"] = ( "Mysql Error %d: %s" % (e.args[0], e.args[1]))
            logging.error ("code=%d msg=%s",  ret["code"], ret["msg"])
    #end readInfo 
    
    def fetchUrl ():
        info["url"] = ( QQ_URL % (info["qq"]))
    #end fetchUrl
    
    def fetchList():
    
        print "download begin ",time.asctime ( time.localtime(time.time()) )
        download ( info, ret)
        if ret["code"] != 0:
            print ret
            return
        #print info["url"]
        info["url"] = ""
        
        
        content = info["content"].split("\n")
        
        strQQ = str(info["qq"])
        groupList = info["groupList"]
        for strLine in content:
            #print strLine
            
            strLine = strLine.strip()
            if len(strLine) == 0:
                continue
            groupInfo = strLine.split(",")
            
            
            #5816859,20872580,姚亚旭,男,成员,5816859,双击查看群信息
            # 0        1       2     3   4    5       6
            #                        l-4  l-3   l-2    l - 1
            
            l = len(groupInfo)
            
            groupList.append({
                "group":int(groupInfo[l-2]),
                "qq":int(groupInfo[1]),
                "nick":",".join(groupInfo[2:l-4]),
                "sex":groupInfo[l-4],
                "role":groupInfo[l-3],
                "name":"",
                "groupState" : 0
            })
    #end fetchList
    
    def save ():
        
        updateQQ(info, ret, conn)
        if ret["code"] != 0:
            print ret
            return
          
        groupList = info["groupList"]
        for groupInfo in groupList:
            updateGroup(groupInfo, ret, conn)
            if ret["code"] != 0:
                print ret
                return
            
        groupList = info["groupList"]
        for groupInfo in groupList:
            updateMap(groupInfo, ret, conn)
            if ret["code"] != 0:
                print ret
                return
    #end save
    
    print "readInfo begin ",time.asctime ( time.localtime(time.time()) )
    readInfo ()
    if ret["code"] != 0:
        print ret
        return
        
    print "fetchUrl begin ",time.asctime ( time.localtime(time.time()) )
    fetchUrl ()
    if ret["code"] != 0:
        print ret
        return
    
    print "fetchList  begin ",time.asctime ( time.localtime(time.time()) )
    fetchList ()
    if ret["code"] != 0:
        print ret
        info["qqState"] = ret["code"]
        ret["code"] = 0
        pass
    
    print "save begin ",time.asctime ( time.localtime(time.time()) )
    save ()
    if ret["code"] != 0:
        print ret
        return
    
#end runQQ


def runGroup(ret, index, conn):
    info = {
        "group" : 0,
        "groupState" : 1,
        "name" : "",
        "qqList" : [],
        "url" : "",
        "content" : ""
    }
    
    def readGroupInfo ():
        try:
            cur = conn.cursor ( )
            sql = "SELECT c_group FROM d_qq.t_group_info_%d where c_state = 0 order by c_group desc limit 1;" % (index)
            cur.execute ( sql)
            results = cur.fetchall ( )
            
            field_names = [ i[0] for i in cur.description ]
            for x in results:
                d = dict ( zip(field_names, list(x)))
                info["group"] = d["c_group"]

            if info["group"] == 0:
                ret["code"] = GROUP_ALL_SEARCH
                ret["msg"] = "all searched"

        except MySQLdb.Error, e:
            ret["code"] = MYSQL_ERROR
            ret["msg"] = ( "Mysql Error %d: %s" % (e.args[0], e.args[1]))
            logging.error ("code=%d msg=%s",  ret["code"], ret["msg"])
    #end readInfo 
    
    def fetchUrl ():
        info["url"] = ( GROUP_URL % (info["group"]))
    #end fetchUrl
    
    def is_number ( uchar):
        #print uchar
        if u'\u00ef' == uchar:
            return False
            
        #判断一个unicode是否是数字
        if uchar >= u'\u0030' and uchar<=u'\u0039':
            return True
        else:
            return False
    
    def fix(strLine):
        while len(strLine) and not strLine[0].isdigit():
            strLine = strLine[1:]
        return strLine
    #end fix
    
    def fetchList():
    
        print "download begin ",time.asctime ( time.localtime(time.time()) )
        download ( info, ret)
        if ret["code"] != 0:
            print ret
            return
        #print info["url"]
        info["url"] = ""
        
        
        content = info["content"].split("\n")
        
        qqList = info["qqList"]
        for strLine in content:
            strLine = strLine.strip()
            if len(strLine) < 4:
                continue
            
            #623966603,永远三六,623966603,单车狂奔,男,成员,1173197,双击查看成员信息
            # 0           1      2         3       4   5    6      7
            #                                     l-4 l-3  l-2     l-1
            
            
            strLine = fix(strLine)
            #print strLine
            
            
            qqInfo = strLine.split(",")
            
            l = len(qqInfo)
            qq = int(qqInfo[0])
            group = int(qqInfo[l-2])
            role = qqInfo[l-3]
            sex = qqInfo[l-4]
            
            strLeft = ",".join(qqInfo[1:l-4])
            #print strLeft, " ", qq
            leftArray = strLeft.split(",%d," % (qq))
            #print leftArray
            if len(leftArray) != 2:
                ret["code"] = STR_EXCEPTION
                return 
            
            info["name"] = leftArray[0]
            nick = leftArray[1]
            
            qqList.append({
                "group":group,
                "qq":qq,
                "nick":nick,
                "sex":sex,
                "role":role,
                "name":info["name"],
                "qqState" : 0
            })
    #end fetchList
    
    def save ():
        
        updateGroup(info, ret, conn)
        if ret["code"] != 0:
            print ret
            return


        qqList = info["qqList"]
        for qqInfo in qqList:
            updateQQ(qqInfo, ret, conn)
            if ret["code"] != 0:
                print ret
                return
            
        qqList = info["qqList"]
        for groupInfo in qqList:
            updateMap(groupInfo, ret, conn)
            if ret["code"] != 0:
                print ret
                return
    #end save
    
    print "readGroupInfo begin ",time.asctime ( time.localtime(time.time()) )
    readGroupInfo ()
    if ret["code"] != 0:
        print ret
        return
        
    print "fetchUrl begin ",time.asctime ( time.localtime(time.time()) )
    fetchUrl ()
    if ret["code"] != 0:
        print ret
        return
    
    print "fetchList  begin ",time.asctime ( time.localtime(time.time()) )
    fetchList ()
    if ret["code"] != 0:
        print ret
        info["groupState"] = ret["code"]
        ret["code"] = 0
        pass
    
    print "save begin ",time.asctime ( time.localtime(time.time()) )
    save ()
    if ret["code"] != 0:
        print ret
        return
#end runGroup


def runHelp(runName, index):
    ret = {
        "code" : 0,
        "msg":"sucess"
    }

    dbcfg = QQ_DBCFG
    conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
    allSearchNum = 0
    while True:
        ret["code"] = 0
        ret["msg"] = "sucess"
        if runName == "QQ":
            runQQ(ret, index, conn)
            if ret["code"] == QQ_ALL_SEARCH:
                time.sleep (10)
                allSearchNum = allSearchNum + 1
            else:
                allSearchNum = 0
        elif runName == "GROUP":
            runGroup(ret, index, conn)
            if ret["code"] == GROUP_ALL_SEARCH:
                time.sleep (10)
                allSearchNum = allSearchNum + 1
            else:
                allSearchNum = 0
        print runName, index
        time.sleep (5)
        if allSearchNum == 10:
            break
#end runQQHelp

def main ( ):

    ret = {
        "code" : 0,
        "msg":"sucess"
    }
    
    print "init begin ",time.asctime ( time.localtime(time.time()) )
    init ( ret)
    
    threads = []
    
    index = 0
    while index < 10:
        threads.append(threading.Thread(target=runHelp, args=("QQ", index)))
        threads.append(threading.Thread(target=runHelp, args=("GROUP", index)))
        index = index + 1
   
    # 启动所有线程
    for t in threads:
        t.start()
        time.sleep (2)
        
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
    if not lockFile("thread.lock.pid"):  
        sys.exit(0) 
    main ( )

