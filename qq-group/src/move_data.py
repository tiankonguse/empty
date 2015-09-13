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
ALL_SEARCH = -9

dbcfg = QQ_DBCFG


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
        #dbcfg = QQ_DBCFG
        #conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        
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


def runQQ(start, end, conn):
    
    infoList = []
    
    ret = {
        "code" : 0,
        "msg":"sucess"
    }
    def readQQInfo ():
        try:
            cur = conn.cursor ( )
            sql = "SELECT c_qq,c_nick,c_sex,c_state FROM t_qq_info where c_qq >= %d and c_qq < %d" % (start, end)
            cur.execute ( sql)
            results = cur.fetchall ( )
            
            field_names = [ i[0] for i in cur.description ]

            
            for x in results:
                d = dict ( zip(field_names, list(x)))            
                info = {
                    "qq" : 0
                }
                info["qq"] = d["c_qq"]
                info["qqState"] = d["c_state"]
                infoList.append(info)
            
            if len(infoList) == 0:
                #print sql
                logging.info(sql)
                ret["code"] = ALL_SEARCH
                ret["msg"] = "all searched"
                
            
        except MySQLdb.Error, e:
            ret["code"] = MYSQL_ERROR
            ret["msg"] = ( "Mysql Error %d: %s sql:%s" % (e.args[0], e.args[1],sql))
            logging.error ("code=%d msg=%s",  ret["code"], ret["msg"])
    #end readQQInfo 
    
    def deleteQQ(info):
        try:
            qq = info["qq"]
            cur = conn.cursor ( )

            sql = ( "DELETE FROM t_qq_info WHERE c_qq=%d" % (qq))
            logging.info(sql)
            cur.execute ( sql)
            conn.commit ( )
        except MySQLdb.Error, e:
            ret["code"] = MYSQL_ERROR
            ret["msg"] = ( "Mysql Error %d: %s sql:%s" % (e.args[0], e.args[1],sql))
            logging.error ( ret["msg"])
    #end deleteQQ
    
    def save (info):
        updateQQ(info, ret, conn)
        if ret["code"] != 0:
            return
          
        deleteQQ(info)
        if ret["code"] != 0:
            return
    #end save
    
    readQQInfo ()
    if ret["code"] != 0:
        #print ret
        return
    
    #print info
    for info in infoList:
        save (info)
        if ret["code"] != 0:
            print ret
            return
    
#end runQQ


def runGroup(start, end, conn):
    infoList = []
    
    ret = {
        "code" : 0,
        "msg":"sucess"
    }
    def readGroupInfo ():
        try:
            cur = conn.cursor ( )
            sql = "SELECT c_group,c_group_name,c_group_info,c_state FROM t_qq_group_info where c_group >= %d and c_group < %d" % (start, end)
            cur.execute ( sql)
            results = cur.fetchall ( )
            
            field_names = [ i[0] for i in cur.description ]

            for x in results:
                d = dict ( zip(field_names, list(x)))
                info = {
                    "group" : 0
                }
                info["group"] = d["c_group"]
                info["name"] = d["c_group_name"]
                info["groupState"] = d["c_state"]
                infoList.append(info)

            if len(infoList) == 0:
                #print sql
                logging.info(sql)
                ret["code"] = ALL_SEARCH
                ret["msg"] = "all searched"
                
            
        except MySQLdb.Error, e:
            ret["code"] = MYSQL_ERROR
            ret["msg"] = ( "Mysql Error %d: %s sql:%s" % (e.args[0], e.args[1],sql))
            logging.error ("code=%d msg=%s",  ret["code"], ret["msg"])
    #end readInfo 
    
    def deleteGroup(info):
        try:
            group = info["group"]
            cur = conn.cursor ( )

            sql = ( "DELETE FROM t_qq_group_info WHERE c_group=%d" % (group))
            logging.info(sql)
            cur.execute ( sql)
            conn.commit ( )
        except MySQLdb.Error, e:
            ret["code"] = MYSQL_ERROR
            ret["msg"] = ( "Mysql Error %d: %s sql:%s" % (e.args[0], e.args[1],sql))
            logging.error ( ret["msg"])
    #end deleteQQ
    
    def save (info):
        
        updateGroup(info, ret, conn)
        if ret["code"] != 0:
            return

        deleteGroup(info)
        if ret["code"] != 0:
            return
    #end save
    
    readGroupInfo ()
    if ret["code"] != 0:
        #print ret
        return
    
    #print info
    for info in infoList:
        save (info)
        if ret["code"] != 0:
            print "save", ret
            return
#end runGroup


def runQQGroup(start, end, conn):
    
    ret = {
        "code" : 0,
        "msg":"sucess"
    }
    infoList = []
    def readQQGroupInfo ():
        try:
            cur = conn.cursor ( )
            sql = "SELECT c_qq,c_group,c_group_nick,c_group_role,c_group_sex from t_qq_group_map where c_qq >= %d and c_qq < %d" % (start, end)
            cur.execute ( sql)
            results = cur.fetchall ( )
            field_names = [ i[0] for i in cur.description ]
            for x in results:
                d = dict ( zip(field_names, list(x)))
                info = {
                    "group" : 0
                }
                info["qq"] = d["c_qq"]
                info["group"] = d["c_group"]
                info["nick"] = d["c_group_nick"]
                info["role"] = d["c_group_role"]
                info["sex"] = d["c_group_sex"]
                infoList.append(info)

            if len(infoList) == 0:
                #print sql
                logging.info(sql)
                ret["code"] = ALL_SEARCH
                ret["msg"] = "all searched"
                
        except MySQLdb.Error, e:
            ret["code"] = MYSQL_ERROR
            ret["msg"] = ( "Mysql Error %d: %s sql:%s" % (e.args[0], e.args[1]),sql)
            logging.error ("code=%d msg=%s",  ret["code"], ret["msg"])
    #end readQQGroupInfo 
    
    def deleteMap(info):
        try:
            group = info["group"]
            qq = info["qq"]
            cur = conn.cursor ( )

            sql = ( "DELETE FROM t_qq_group_map WHERE c_qq=%d and c_group=%d" % (qq, group))
            logging.info(sql)
            cur.execute ( sql)
            conn.commit ( )
        except MySQLdb.Error, e:
            ret["code"] = MYSQL_ERROR
            ret["msg"] = ( "Mysql Error %d: %s sql:%s" % (e.args[0], e.args[1]),sql)
            logging.error ( ret["msg"])
    #end deleteMap
    
    def save (info):
        
        updateMap(info, ret, conn)
        if ret["code"] != 0:
            return

        deleteMap(info)
        if ret["code"] != 0:
            return
    #end save
    
    readQQGroupInfo ()
    if ret["code"] != 0:
        #print ret
        return
    #print info
    for info in infoList:
        save (info)
        if ret["code"] != 0:
            print ret
            return
#end runQQGroup



def threadHelp(ret, info, fun, connPool):
    threads = []

    index = 0
    threadNum = info["threadNum"]
    step = info["step"]
    start = info["start"]
    while index < threadNum:
        end = start+step
        threads.append(threading.Thread(target=fun, args=(start, end, connPool[index])))
        start = end
        index = index + 1
        
    info["start"] = start
    
    # 启动所有线程
    for t in threads:
        t.start()
        
    # 主线程中等待所有子线程退出
    for t in threads:
        t.join()  
    
#end threadHelp




def runHelp(runName, index):
    print "runHelp"
    
    ret = {
        "code" : 0,
        "msg":"sucess"
    }
    
    info = {
        "start" : 0,
        "threadNum" : 780,
        "step" : 1000,
    }
    
    def updateStart():
        bcfg = QQ_DBCFG
        conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        sql = ""
        try:
            cur = conn.cursor ( )
            if runName == "QQ":
                info["step"] = 10000
                sql = "SELECT c_qq as start FROM t_qq_info order by c_qq limit 1"
            elif runName == "GROUP":
                info["step"] = 5000
                sql = "SELECT c_group as start FROM t_qq_group_info order by c_group limit 1"
            elif runName == "QQ_GROUP":
                info["step"] = 10000
                sql = "SELECT c_qq as start FROM t_qq_group_map order by c_qq limit 1"
            cur.execute ( sql)
            results = cur.fetchall ( )
            
            field_names = [ i[0] for i in cur.description ]

            info["start"] = 0
            for x in results:
                d = dict ( zip(field_names, list(x)))            
                info["start"] = d["start"]
            
        except MySQLdb.Error, e:
            ret["code"] = MYSQL_ERROR
            ret["msg"] = ( "Mysql Error %d: %s sql:%s" % (e.args[0], e.args[1],sql))
            logging.error ("code=%d msg=%s",  ret["code"], ret["msg"])
            
        conn.close()
    
    
    connPool = []
    index = 0
    while index < info["threadNum"]:
        dbcfg = QQ_DBCFG
        conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        connPool.append(conn)
        index = index + 1
    
    print runName
    while True:
        ret["code"] = 0
        ret["msg"] = "sucess"
        updateStart()
        if info["start"] == 0:
            break
            
        if runName == "QQ":
            threadHelp(ret, info, runQQ, connPool)
        elif runName == "GROUP":
            threadHelp(ret, info,runGroup, connPool)
        elif runName == "QQ_GROUP":
            threadHelp(ret, info, runQQGroup, connPool)
        
        print time.asctime ( time.localtime(time.time()) ),info["start"],runName,ret
        if info["start"] > 99999999999L:
            break
        time.sleep (1)
        
    index = 0
    while index < info["threadNum"]:
        connPool[index].close()
        index = index + 1
#end runQQHelp

def main ( ):

    ret = {
        "code" : 0,
        "msg":"sucess"
    }
    
    print "init begin ",time.asctime ( time.localtime(time.time()) )
    init ( ret)
    
    threads = []
    
    print "thread"
    
    #threads.append(threading.Thread(target=runHelp, args=("QQ", 1)))
    #threads.append(threading.Thread(target=runHelp, args=("GROUP", 2)))
    threads.append(threading.Thread(target=runHelp, args=("QQ_GROUP", 3)))
    
    
    # 启动所有线程
    for t in threads:
        t.start()
        
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
    if not lockFile("move_data.lock.pid"):  
        sys.exit(0) 
    main ( )

