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
from bs4 import BeautifulSoup

import fcntl  


useragent = {
    'User-Agent':'Mozilla/5.0 ( Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
    'X-Forwarde-For':'127.0.0.1',
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-language' : 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    'x-chrome-uma-enabled' : '1',
    'x-client-data' : 'CKa1yQEIi7bJAQiltskBCKm2yQEInpLKARiricoB',
    'cookie': 'SID=DQAAABkBAACUbUYZdJooXg7-9GI_j3oD7smGLqqcuPtMKc8wmBnlDRXrDOE0xi9kFRAKuPlX4M47-d5RJdkovuotso5l2KWCTTUzxxtZqJc1sh1jqqTZuKXjgR8w4BFAlveW3fvcX-mI9C1sOAnrxVtslS8vVVGzEf_edZZejnfP0vi37q18BxVXcWiG65HbtIK424S979wIlwRGfojYx4iNdLtA3H7YdiYg53CfuDMZHurNnYuUgWhNxwzvy8sswpqfPRGYD-Wh8oXnUK44BK8ZWdepEIZV7CAYsdTzh1j8LrCu49r1vNTeq04nwPqljvmXljGYto3pxToJOtM_XcycxpcCbMVGbQgYV9cvVaCII3B2Csh6DafbsNK80PqWEP2XFclim14; HSID=AAimToEO1TIVrCvCg; SSID=AMl8VcHM4SkyFcDc0; APISID=vxfEmWuSZYA3wxvp/A3ErMswXj2cDLLADn; SAPISID=R3VT_BX_5rVhEOvr/A1bnJvguY5V3RiNvz; NID=67=tdZOOjZBFB-Yb5BsE_ze3NE6uEXjMF2GyEI0AxoCdtdcwRKTXbZXwhYb00neOXHCE4ZxVXT0lpMdvN8onmUjzUJTprFUZek2r3FPEajXZsdQlsDstEhz3EeEA2Vf3FbCFxOJl_4VBqaBsugTJUhYuszCir_gJD8sDujARrxAkKBoRlD_w1qPbhZUWjjv7DsUcIJ0GAaIJ_YYIYQMBzJECt4IBgdp6sfobUq20vNVB7UMrPvw-QiGM2v5hCQ5QmdeaaOFcRuIhw6Rws_8; __utmt_siteTracker=1; __utmt_projectTracker=1; __utma=247248150.483320998.1426387355.1426872237.1426908099.11; __utmb=247248150.22.10.1426908099; __utmc=247248150; __utmz=247248150.1426434967.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); PREF=ID=87dacd255b8d778c:U=199e11645c738924:FF=1:LD=zh-CN:NR=10:NW=1:TM=1426088873:LM=1426912111:GM=1:SG=1:S=TtZ2A7GtUixL1atw'
}



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


SEARCH_URL = 'https://code.google.com/hosting/search?q=label:%s&filter=0&mode=&start=%d'
HOME_URL = 'https://code.google.com/p/%s/'
CHECKOUT_URL = 'https://code.google.com/p/%s/source/checkout'
CLONE_URL = 'https://code.google.com/r/%s/source/clones'
MEMBER_LIST_URL = 'https://code.google.com/p/%s/people/list?num=5000&start=0' 

HTTP_CODE = [404, 403, 500, 301]
HTTP_CORE_DOWN = [301]

def init ( ret):

    reload ( sys)
    sys.setdefaultencoding ( 'utf8')

    today = datetime.date.today ( )
    logfilepath = "../log/" + os.path.splitext ( os.path.basename(__file__))[0] + "_" + today.strftime('%Y%m%d') + ".log"
    logging.basicConfig ( filename=logfilepath, level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s: %(message)s')

    socks.setdefaultproxy ( socks.PROXY_TYPE_SOCKS5, PROXY["ip"], PROXY["port"])
    socket.socket = socks.socksocket

#end init


def myrand ( ):
    return random.randint ( 1, 126)
#end myrand

def rand_ip ( ):
    return ( "127.%d.%d.%d`" % (myrand(), myrand(),myrand()))
#rand_ip

def download ( info, ret):
    try:
        url = info["url"]
        useragent['X-Forwarde-For'] = rand_ip ( )
        req = urllib2.Request ( url, None, useragent)
        info["content"] = urllib2.urlopen ( req,  timeout=2).read()

    except urllib2.HTTPError, e:
        ret["code"] = -1
        ret["msg"] = ( '(%s)http request error code - %s.' % (url, e.code))
        if e.code in HTTP_CODE:
            ret["code"] = e.code
            
    except urllib2.URLError, e:
        ret["code"] = -1
        ret["msg"] = ( '(%s)http request error reason - %s.' % (url, e.reason))
    except Exception:
        ret["code"] = -1
        ret["msg"] = ( '(%s)http request generic exception: %s.' % (url, traceback.format_exc()))
#end test


def is_chinese ( uchar):
    #判断一个unicode是否是汉字
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

def is_number ( uchar):
    #判断一个unicode是否是数字
    if uchar >= u'\u0030' and uchar<=u'\u0039':
        return True
    else:
        return False


def is_alphabet ( uchar):
    #判断一个unicode是否是英文字母
    if ( uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
        return True
    else:
        return False

def is_ascii ( uchar):
    #判断一个unicode是否是ascii
    if ( uchar >= u'\u0000' and uchar<=u'\u00ef'):
        return True
    else:
        return False
#end is_ascii


def is_fetch_char ( uchar):
    if ( is_ascii(uchar) or is_chinese(uchar)):
        return True
    else:
        return False
#end is_fetch_char


def addLableByName ( lableName, ret):
    try:
        dbcfg = GOOGLE_CODE_DBCFG
        conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor ( )

        lableName = conn.escape_string ( lableName)

        sql = ( "SELECT count(*) FROM d_google_code_backup.t_lable where c_name = '%s';" % (lableName))
        cur.execute ( sql)
        results = cur.fetchall ( )
        count = 0
        for x in results:
            count = x[0]

        if count != 0 :
            return

        sql = ( "INSERT INTO `d_google_code_backup`.`t_lable` (`c_name`, `c_search_page`, `c_max_num`) VALUES ('%s', '0', '0');" % (lableName))
        cur.execute ( sql)
        logging.debug ( sql)
        conn.commit ( )
        conn.close ( )
    except MySQLdb.Error, e:
        ret["code"] = -1
        ret["msg"] = ( "Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error ( ret["msg"])
#end addLableByName

def addProjectByName ( prjName, ret):
    try:
        dbcfg = GOOGLE_CODE_DBCFG
        conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor ( )

        prjName = conn.escape_string ( prjName)

        sql = ( "SELECT count(*) FROM d_google_code_backup.t_project where c_name = '%s';" % (prjName))
        cur.execute ( sql)
        results = cur.fetchall ( )
        count = 0
        for x in results:
            count = x[0]

        if count != 0 :
            return

        sql = ( "INSERT INTO `d_google_code_backup`.`t_project` (`c_name`, `c_starred_num`, `c_members_num`, `c_ok`) VALUES ('%s', 0, 0, 0);" % (prjName))
        cur.execute ( sql)
        logging.debug ( sql)
        conn.commit ( )
        conn.close ( )
    except MySQLdb.Error, e:
        ret["code"] = -1
        ret["msg"] = ( "Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error ( ret["msg"])
#addPrijectByName


def addMemberByName ( memberName, ret):
    try:
        dbcfg = GOOGLE_CODE_DBCFG
        conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor ( )

        memberName = conn.escape_string ( memberName)

        sql = ( "SELECT count(*) FROM d_google_code_backup.t_user where c_name = '%s';" % (memberName))
        cur.execute ( sql)
        results = cur.fetchall ( )
        count = 0
        for x in results:
            count = x[0]

        if count != 0 :
            return

        sql = ( "INSERT INTO `d_google_code_backup`.`t_user` (`c_name`, `c_projects_num`, `c_starred_num`, `c_ok`) VALUES ('%s', 0, 0, 0);" % (memberName))
        cur.execute ( sql)
        logging.debug ( sql)
        conn.commit ( )
        conn.close ( )
    except MySQLdb.Error, e:
        ret["code"] = -1
        ret["msg"] = ( "Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error ( ret["msg"])
#end addMemberByName

def connectLableProject ( lableName, prjName, ret):
    try:
        addLableByName ( lableName, ret)
        if ret["code"] != 0:
            print ret
            return

        addProjectByName ( prjName, ret)
        if ret["code"] != 0:
            print ret
            return

        dbcfg = GOOGLE_CODE_DBCFG
        conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor ( )

        lableName = conn.escape_string ( lableName)
        prjName = conn.escape_string ( prjName)
        sql = ( "SELECT count(*) FROM d_google_code_backup.t_prj_lable where c_prj_name='%s' and c_lable_name = '%s';" % (prjName, lableName))
        cur.execute ( sql)
        results = cur.fetchall ( )
        count = 0
        for x in results:
            count = x[0]

        if count != 0 :
            return

        sql = ( "INSERT INTO `d_google_code_backup`.`t_prj_lable` (`c_prj_name`, `c_lable_name`) VALUES ('%s', '%s');" % (prjName, lableName))
        cur.execute ( sql)
        logging.debug ( sql)
        conn.commit ( )
        conn.close ( )
    except MySQLdb.Error, e:
        ret["code"] = -1
        ret["msg"] = ( "Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error ( ret["msg"])
#end connectLableProject


def connecMemberProject(memberName,prjName, ret):
    try:
        addMemberByName ( memberName, ret)
        if ret["code"] != 0:
            print ret
            return

        addProjectByName ( prjName, ret)
        if ret["code"] != 0:
            print ret
            return

        dbcfg = GOOGLE_CODE_DBCFG
        conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor ( )

        memberName = conn.escape_string ( memberName)
        prjName = conn.escape_string ( prjName)
        sql = ( "SELECT count(*) FROM d_google_code_backup.t_prj_user where c_prj_name='%s' and c_user_name='%s';" % (prjName, memberName))
        cur.execute ( sql)
        results = cur.fetchall ( )
        count = 0
        for x in results:
            count = x[0]

        if count != 0 :
            return

        sql = ( "INSERT INTO `d_google_code_backup`.`t_prj_user` (`c_prj_name`, `c_user_name`) VALUES ('%s', '%s');" % (prjName, memberName))
        cur.execute ( sql)
        logging.debug ( sql)
        conn.commit ( )
        conn.close ( )
    except MySQLdb.Error, e:
        ret["code"] = -1
        ret["msg"] = ( "Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error ( ret["msg"])
#end connecMemberProject


def updateLable ( info, ret):
    try:
        dbcfg = GOOGLE_CODE_DBCFG
        conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor ( )

        id = info["id"]
        nowNum = info["nowNum"]
        maxNum = info["maxNum"]
        ok = info["ok"]

        sql = ( "update d_google_code_backup.t_lable set c_search_page = %d , c_max_num = %d, c_ok = %d where c_id = %d;" % (nowNum, maxNum, ok, id))
        logging.debug ( sql)
        cur.execute ( sql)
        conn.commit ( )
        conn.close ( )
    except MySQLdb.Error, e:
        ret["code"] = -1
        ret["msg"] = ( "Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error ( ret["msg"])
#end updateLable



def updateProject ( info, ret):
    try:
        dbcfg = GOOGLE_CODE_DBCFG
        conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor ( )

        id = info["id"]
        starNum = info["starNum"]
        memberNum = info["memberNum"]
        clones = info["clones"]
        ok = info["ok"]
        checkout = conn.escape_string ( info["checkout"])
        desc = conn.escape_string ( (info["desc"]))
        parent = conn.escape_string ( (info["parent"]))

        sql = ( "UPDATE `d_google_code_backup`.`t_project` SET `c_starred_num`=%d, `c_members_num`=%d, `c_ok`=%d, `c_clones`=%d, `c_checkout`='%s', `c_desc`='%s', `c_parent`='%s' WHERE `c_id`=%d;" % (starNum, memberNum, ok,  clones, checkout, desc, parent, id))
        logging.debug ( sql)
        cur.execute ( sql)
        conn.commit ( )
        conn.close ( )
    except MySQLdb.Error, e:
        ret["code"] = -1
        ret["msg"] = ( "Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error ( ret["msg"])
#end updateProject


def runLable ( ret):
    lableInfo = {
        "id" : 0,
        "ok" : 0,
        "lableName" : "",
        "nowNum" : 0,
        "maxNum" : 0,
        "url" : "",
        "content" : "",
        "prjList" : []
    }


    def readLableInfo ( lableInfo, ret):
        try:
            dbcfg = GOOGLE_CODE_DBCFG
            conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
            cur = conn.cursor ( )
            sql = "SELECT c_id as id, c_name as name, c_search_page as nowNum, c_max_num as maxNum FROM d_google_code_backup.t_lable where (c_max_num = 0 or c_search_page < c_max_num) and c_ok = 0 limit 1;"
            cur.execute ( sql)
            results = cur.fetchall ( )
            field_names = [ i[0] for i in cur.description ]
            
            for x in results:
                d = dict ( zip(field_names, list(x)))
                lableInfo["id"] = d["id"]
                lableInfo["lableName"] = d["name"]
                lableInfo["nowNum"] = d["nowNum"]
                lableInfo["maxNum"] = d["maxNum"]

            if lableInfo["id"] == 0:
                ret["code"] = -2
                ret["msg"] = "all searched"

            conn.close ( )
        except MySQLdb.Error, e:
            ret["code"] = -1
            ret["msg"] = ( "Mysql Error %d: %s" % (e.args[0], e.args[1]))
            logging.error ( ret["msg"])
    #end fetchMatchState


    def getSearchUrl ( lableInfo, ret):
        lableInfo["url"] = ( SEARCH_URL % (lableInfo["lableName"], lableInfo["nowNum"]))
    #end getSearchUrl

    def fetchPrjList ( info, ret):
        prjList = info["prjList"]
        soup = BeautifulSoup ( info["content"])
        info["content"] = ""
        
        if info["maxNum"] == 0:
            tdList = soup.find ( attrs={"class": "mainhdr"}).findAll("td")
            if len ( tdList) == 0:
                info["ok"] = 1
                return
            info["maxNum"] = tdList[1].string.strip ( ).split(' ')[-1]
            info["maxNum"] = int ( info["maxNum"])

        serp = soup.find ( id='serp')

        tableList = serp.findAll ( 'table')



        for table in tableList:
            prj = {
                "prjName" : "",
                "lableList" : []
            }
            lableList = prj["lableList"]

            tdList = table.findAll ( 'td')

            prjLink = tdList[0].find ( 'a')["href"]

            prj["prjName"] = prjLink[3:-1]

            info["nowNum"] = info["nowNum"] + 1

            if not is_fetch_char ( prj["prjName"]):
                continue

            ptjLableLink = tdList[1].find ( attrs={"class": "labels"}).findAll("a")

            for link in ptjLableLink:
                lableName = link.string
                if not is_fetch_char ( lableName):
                    continue
                lableList.append ( lableName)

            prjList.append ( prj)
    #end fetchPrjList



    def saveLableInfo ( info, ret):
        lableName = info["lableName"]

        prjList = info["prjList"]
        for prj in prjList:
            prjName = prj["prjName"]
            connectLableProject ( lableName, prjName, ret)
            if ret["code"] != 0:
                print ret
                return
            lableList = prj["lableList"]
            for prjLableName in lableList:
                connectLableProject ( prjLableName, prjName, ret)
                if ret["code"] != 0:
                    print ret
                    return

        updateLable ( info, ret)

        if ret["code"] != 0:
            print ret
            return
    #end saveLableInfo


    print "readLableInfo begin ",time.asctime ( time.localtime(time.time()) )
    readLableInfo ( lableInfo, ret)
    if ret["code"] != 0:
        print ret
        return
    

    print "getSearchUrl begin ",time.asctime ( time.localtime(time.time()) )
    getSearchUrl ( lableInfo, ret)
    if ret["code"] != 0:
        print ret
        return
    #print lableInfo
    
    print "download begin ",time.asctime ( time.localtime(time.time()) )
    download ( lableInfo, ret)
    if not (ret["code"] == 0 or ret["code"] in HTTP_CODE):
        print ret
        return
    else:
        lableInfo["ok"] = 1
    
    if (ret["code"] not in HTTP_CODE) or lableInfo["ok"] == 1:
        print "fetchPrjList begin ",time.asctime ( time.localtime(time.time()) )
        fetchPrjList ( lableInfo, ret)
        if ret["code"] != 0:
            print ret
            return
    else:
        lableInfo["ok"] = 1
    ret["code"] = 0
    
    #print lableInfo
    
    print "saveLableInfo begin ",time.asctime ( time.localtime(time.time()) )
    saveLableInfo ( lableInfo, ret)
    if ret["code"] != 0:
        print ret
        return
#end run



def runProject ( ret):
    prjInfo = {
        "id" : 0,
        "prjName" : "",
        "starNum" : 0,
        "memberNum" : 0,
        "ok" : "",
        "clones" : 0,
        "checkout" : "",
        "desc" : "",
        "lableList" : [],
        "memberList" : [],
        "clonesList" : [],
        "parent" : "",
        "url" : "",
        "content" : ""
    }

    
    def readProjectInfo ( prjInfo, ret):
        try:
            dbcfg = GOOGLE_CODE_DBCFG
            conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
            cur = conn.cursor ( )
            #sql = "SELECT c_id as id, c_name as prjName,c_starred_num as starNum,c_members_num as memberNum,c_ok as ok,c_clones as clones,c_checkout as checkout,c_desc as description FROM d_google_code_backup.t_project where c_ok = 0 and c_clones = 0 and c_parent = '' limit 1;"
            sql = "SELECT c_id as id, c_name as prjName,c_starred_num as starNum,c_members_num as memberNum,c_ok as ok,c_clones as clones,c_checkout as checkout,c_desc as description FROM d_google_code_backup.t_project where c_ok in (1,2) and c_checkout='' and c_parent='' limit 1;"
            cur.execute ( sql)
            results = cur.fetchall ( )
            
            field_names = [ i[0] for i in cur.description ]
            for x in results:
                d = dict ( zip(field_names, list(x)))
                prjInfo["id"] = d["id"]
                prjInfo["prjName"] = d["prjName"]
                prjInfo["starNum"] = d["starNum"]
                prjInfo["memberNum"] = d["memberNum"]
                prjInfo["ok"] = 1
                prjInfo["clones"] = d["clones"]
                prjInfo["checkout"] = d["checkout"]
                prjInfo["desc"] = d["description"]

            if prjInfo["id"] == 0:
                ret["code"] = -2
                ret["msg"] = "all searched"

            conn.close ( )
        except MySQLdb.Error, e:
            ret["code"] = -1
            ret["msg"] = ( "Mysql Error %d: %s" % (e.args[0], e.args[1]))
            logging.error ( ret["msg"])
    #end readProjectInfo    
    
    def getHomeUrl ( prjInfo, ret):
        prjInfo["url"] = ( HOME_URL % (prjInfo["prjName"]))
    #end getHomeUrl

    
    def getCheckoutUrl ( prjInfo, ret):
        prjInfo["url"] = ( CHECKOUT_URL % (prjInfo["prjName"]))
    #end getHomeUrl

    def getCloneUrl ( prjInfo, ret):
        prjInfo["url"] = ( CLONE_URL % (prjInfo["prjName"]))
    #end getCloneUrl

    def fetchHomeInfo ( prjInfo, ret):
        print "getHomeUrl begin ",time.asctime ( time.localtime(time.time()) )
        getHomeUrl ( prjInfo, ret)
        if ret["code"] != 0:
            print ret
            return
            
        print "download begin ",time.asctime ( time.localtime(time.time()) )
        download ( prjInfo, ret)
        if not (ret["code"] == 0 or ret["code"] in HTTP_CODE):
            print ret
            return
        
        if ret["code"] in HTTP_CODE:
            # 404, 403
            ret["code"] = 0
            prjInfo["ok"] = ret["code"]
            return
        print prjInfo["url"]
        prjInfo["url"] = ""
       
        soup = BeautifulSoup ( prjInfo["content"])
        prjInfo["content"] = ""
        
        if not soup.find ( id='pname'):
            # move to github
            prjInfo["ok"] = -1
            return
                               
        starNode = soup.find ( id="star_count")
        if starNode and  prjInfo["starNum"] == 0:
            prjInfo["starNum"] = int ( starNode.string)
        
        descNode = soup.find ( attrs={"itemprop": "description"})
        if descNode :
            prjInfo["desc"] = descNode.string
        
        lableListLink = soup.find_all ( "a", attrs={"class": "label"})
        if lableListLink:
            lableList = prjInfo["lableList"]
            for lableLink in lableListLink:
                lableName = lableLink.string
                if not is_fetch_char ( lableName):
                    continue
                lableList.append ( lableName)  
    #end fetchHomeInfo


    def getText ( node):
        return "".join ( re.split("<[^>]*>", str(node))).strip() 
    #end getText

    def fetchCheckoutInfo ( prjInfo, ret):
        print "getCheckoutUrl begin ",time.asctime ( time.localtime(time.time()) )
        getCheckoutUrl ( prjInfo, ret)
        if ret["code"] != 0:
            print ret
            return
            
        print "download begin ",time.asctime ( time.localtime(time.time()) )
        download ( prjInfo, ret)
        if not (ret["code"] == 0 or ret["code"] in HTTP_CODE):
            print ret
            return
        print prjInfo["url"]
        prjInfo["url"] = ""
       
        if ret["code"] in HTTP_CODE:
            prjInfo["ok"] = ret["code"]
            ret["code"] = 0
            return
       
        soup = BeautifulSoup ( prjInfo["content"])
        prjInfo["content"] = ""
        
        if not soup.find ( id='pname'):
            prjInfo["ok"] = -1
            return
        
        prjInfo["checkout"] = getText ( soup.find(attrs={"id": "checkoutcmd"}))
    #end fetchCheckoutInfo
    
    def fetchCloneInfo ( prjInfo, ret):
        print "getCloneUrl begin ",time.asctime ( time.localtime(time.time()) )
        getCloneUrl ( prjInfo, ret)
        if ret["code"] != 0:
            print ret
            return
            
        print "download begin ",time.asctime ( time.localtime(time.time()) )
        download ( prjInfo, ret)
        if not (ret["code"] == 0 or ret["code"] in HTTP_CODE):
            print ret
            return
        print prjInfo["url"]
        prjInfo["url"] = ""
        
        if ret["code"] in HTTP_CODE:
            prjInfo["ok"] = ret["code"]
            ret["code"] = 0
            return
        
        soup = BeautifulSoup ( prjInfo["content"])
        prjInfo["content"] = ""
        
        if not soup.find ( id='pname'):
            prjInfo["ok"] = -1
            return
        
        
        resultstable = soup.find ( id='resultstable')
   
        clonesList = prjInfo["clonesList"]
        
        trList = resultstable.find_all ( "tr")
        
        
        if len ( trList) >= 3:
            tdList = trList[2].find_all ( "td")
            tdLen = len ( tdList)
            tdText = getText ( tdList[0])
            if tdLen == 1 and len ( tdText) > 9 and tdText[0:9] == "Clones of":
                # have Parent
                print "have Parent"
                prjInfo["parent"] = trList[1].find ( "a")["href"].split("/")[2]
                prjInfo["clones"] = 1
                trList = trList[3:]
            

        if resultstable.find ( attrs={"class": "id"}):
            #no child
            return
        
        #have child
        if prjInfo["clones"]== 0:
            trList = trList[1:]
            
        for tr in trList:
             clonesList.append ( tr.find_all("td")[1].find("a")["href"].split("/")[2])
    #end fetchCloneInfo
  
    def getMemberListUrl ( prjInfo, ret):
        prjInfo["url"] = ( MEMBER_LIST_URL % (prjInfo["prjName"]))
    #end getMemberListUrl

    def fetchMemberList ( prjInfo, ret):
        print "getMemberListUrl begin ",time.asctime ( time.localtime(time.time()) )
        getMemberListUrl ( prjInfo, ret)
        if ret["code"] != 0:
            print ret
            return
            
        print "download begin ",time.asctime ( time.localtime(time.time()) )
        download ( prjInfo, ret)
        if not (ret["code"] == 0 or ret["code"] in HTTP_CODE):
            print ret
            return
        print prjInfo["url"]
        prjInfo["url"] = ""
        
        if ret["code"] in HTTP_CODE:
            prjInfo["ok"] = ret["code"]
            ret["code"] = 0
            return
        
        soup = BeautifulSoup ( prjInfo["content"])
        prjInfo["content"] = ""
        
        
        if not soup.find ( id='pname'):
            prjInfo["ok"] = -1
            return


        tdListNode = soup.find(id='resultstable').find_all( attrs = {"class":"col_0"})
        
        memberList = prjInfo["memberList"]
        for tdNode in tdListNode:
            memberList.append( tdNode.find("a")["href"].split("=")[-1])
        
        paginationNode = soup.find( attrs = {"class":"pagination"})
        if paginationNode.find("a"):
            memberNum = len(memberList)
        else:
            memberNum = int(paginationNode.string.strip().split(" ")[-1])
        prjInfo["memberNum"] = memberNum 

    #end fetchMemberList 
    
    
    def updateCloneProject(clonePrjName,prjName, ret):
        addProjectByName(clonePrjName, ret)
        if ret["code"] != 0:
            print ret
            return
        
        try:
            dbcfg = GOOGLE_CODE_DBCFG
            conn = MySQLdb.connect ( host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
            cur = conn.cursor ( )

            clonePrjName = conn.escape_string (clonePrjName)
            prjName = conn.escape_string (prjName)

            sql = ( "UPDATE `d_google_code_backup`.`t_project` SET `c_ok`=1, `c_parent`='%s' WHERE `c_name`='%s';" % (prjName, clonePrjName))
            logging.debug ( sql)
            cur.execute ( sql)
            conn.commit ( )
            conn.close ( )
        except MySQLdb.Error, e:
            ret["code"] = -1
            ret["msg"] = ( "Mysql Error %d: %s" % (e.args[0], e.args[1]))
            logging.error ( ret["msg"])
    #end updateCloneProject
    
    def saveProject( prjInfo, ret):
        prjName = prjInfo["prjName"]
        
        lableList = prjInfo["lableList"]
        for lableName in lableList:
            connectLableProject(lableName,prjName, ret)
            if ret["code"] != 0:
                print ret
                return
        
        clonesList = prjInfo["clonesList"]
        for clonePrjName in clonesList:
            updateCloneProject(clonePrjName,prjName, ret)
            if ret["code"] != 0:
                print ret
                return
        
        memberList = prjInfo["memberList"]
        for memberName in memberList:
            connecMemberProject(memberName,prjName, ret)
            if ret["code"] != 0:
                print ret
                return
        
        updateProject ( prjInfo, ret)
        if ret["code"] != 0:
            print ret
            return
    #end saveProject

    print "readProjectInfo begin ",time.asctime ( time.localtime(time.time()) )
    readProjectInfo ( prjInfo, ret)
    if ret["code"] != 0:
        print ret
        return

    print "fetchHomeInfo begin ",time.asctime ( time.localtime(time.time()) )
    fetchHomeInfo ( prjInfo, ret)
    
    if ret["code"] == 0 and prjInfo["ok"] not in HTTP_CORE_DOWN:
        print "fetchMemberList  begin ",time.asctime ( time.localtime(time.time()) )
        fetchMemberList ( prjInfo, ret)
    else:
        print ret
    
    
    if ret["code"] == 0 and prjInfo["ok"] not in HTTP_CORE_DOWN :
        print "fetchCheckoutInfo begin ",time.asctime ( time.localtime(time.time()) )
        fetchCheckoutInfo ( prjInfo, ret)
    else:
        print ret
        
        
    if ret["code"] == 0 and prjInfo["ok"] not in HTTP_CORE_DOWN:
        print "fetchCloneInfo begin ",time.asctime ( time.localtime(time.time()) )
        fetchCloneInfo ( prjInfo, ret)
    else:
        print ret
        
        
        
    if ret["code"] == -2:
        print ret
        return

    #print prjInfo
    #print json.dumps(prjInfo, sort_keys=True, indent=2)
    print "saveProject begin ",time.asctime ( time.localtime(time.time()) )
    saveProject ( prjInfo, ret)
    if ret["code"] != 0:
        print ret
        return
#end runProject


def main ( ):

    ret = {
        "code" : 0,
        "msg":"sucess"
    }



    print "init begin ",time.asctime ( time.localtime(time.time()) )
    init ( ret)


    if ret["code"] != 0:
        print ret
        return

    while True:
        realRun = 0 
        
        ret["code"] = 0
        #runLable ( ret)
        #if ret["code"] == -1:
        #    print ret
        #    return
        #elif ret["code"] == 0:
        #    realRun = 1
        
        
        ret["code"] = 0
        runProject ( ret)
        if ret["code"] == -1:
            print ret
            return
        elif ret["code"] == 0:
            realRun = 1
            
        if realRun == 0:
            print "search end"
            return
        time.sleep (0.001)
        
#end main
def lockFile(lockfile):  
    #fp = open(lockfile, 'w')  
    fp = os.open(lockfile, os.O_CREAT | os.O_TRUNC | os.O_WRONLY)
    try:  
        fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)  
        print ("lockFile ok ")
    except IOError, e:
        print ("lockFile error %d=s %s" % (e.args[0], e.args[1]))
        return False  
    return True 
if __name__ == "__main__":
    if not lockFile(".lock.pid"):  
        sys.exit(0) 
    main ( )
