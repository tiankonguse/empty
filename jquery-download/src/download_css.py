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
#from BeautifulSoup import BeautifulSoup

import fcntl  


useragent = {
    'Host':'hemin.cn',
    'X-Forwarde-For':'195.154.92.79',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-language' : 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    'Upgrade-Insecure-Requests' : '1',
    'Referer' : 'http://hemin.cn/jq/index.html',
    'cookie': 'Hm_lvt_27646e8f048a16e17f027842e6bdb8f0=1444552476,1444554233; Hm_lpvt_27646e8f048a16e17f027842e6bdb8f0=1444555320; PHPSESSID=43df5109ec592b138e49102b1fa19568; Hm_lvt_f01bb17e7dba8f1fef821e31e44f4fec=1444554291; Hm_lpvt_f01bb17e7dba8f1fef821e31e44f4fec=1444554291'
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


HOME_URL = "http://hemin.cn/css/"


HTTP_CODE = [404, 403, 500, 301]
HTTP_CORE_DOWN = [301]

GROUP_ALL_SEARCH = -2
MYSQL_ERROR = -3
QQ_ALL_SEARCH = -4
URL_ERROR = -5
DOWNLOAD_EXCEPTION = -6
HTTP_ERROR = -7
STR_EXCEPTION = -8



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


def save(name, title, description, keywords, content):
    filePath = ("../data/css/%s" % (name))
    try:
        f = open(filePath, 'w')
        f.write("---\n")
        f.write("layout: css\n")
        f.write("title: %s\n"%(title))
        f.write("description: %s\n"%(description))
        f.write("keywords: %s\n"%(keywords))
        f.write("---\n")
        f.write("\n")
        f.write("\n")
        f.write("%s\n"%(content))
        f.write("\n")
        f.close()
        return 0
    except IOError, e:
        logging.error("Error %d: %s" % (e.args[0], e.args[1]))
        return 1
def downjQuery(link, pre):
    ret = {
        "code" : 0,
        "msg":"sucess"
    }
    print link
    info = {
        "url" : HOME_URL + link,
        "content" : ""
    }
    download ( info, ret)
    if ret["code"] != 0:
        print ret, link
        return
        
    #html
    soup = BeautifulSoup(info["content"])
    
    
    # content
    content = soup.findAll(id="content")
    strContent = str(content[0])
    soupContent = BeautifulSoup(str(strContent))
    
    if len(soupContent) == 0:
        print "soupContent is empty"
        return
    
    
    if soupContent.iframe:
        soupContent.iframe.extract()
    
    strContent =  str(soupContent.html.body.contents[0])
    
    #title
    
    
    title = soup.findAll("title")
    
    if (not title) or len(title) == 0:
        title = link
    else:
        title = title[0].string
        
    title = pre + title
    
    #description
    description = " css CSS中文手册(在线版)"
    
    #keywords
    keywords = soup.findAll("meta",{"name" : "keywords"})
    if (not keywords) or len(keywords) == 0:
        keywords = ""
    else:
        keywords = keywords[0].get("content")
    keywords = pre + keywords
    
    if save(link, title, description, keywords, strContent):
        print "save error", link
        return
        
def main ( ):
    aMap = set()
    
    ret = {
        "code" : 0,
        "msg":"sucess"
    }
    
    print "init begin ",time.asctime ( time.localtime(time.time()) )
    init ( ret)

    
    info = {
        "url" : HOME_URL,
        "content" : ""
    }
    download ( info, ret)
    aMap.add(info["url"])
    
    if ret["code"] != 0:
        print ret
        return
        
    #html
    soup = BeautifulSoup(info["content"])
    
    
    # content
    content = soup.findAll(id="contentA2")
    soupContent = BeautifulSoup(str(content))
    
    if len(soupContent) == 0:
        print "soupContent is empty"
        return
    
    # ul
    ul = soupContent.findAll("ul")
    soupUl = BeautifulSoup(str(ul))
    
    # links
    aList = soupUl.findAll("a")
    
    for a in aList:
        if a in aMap:
            continue
        aMap.add(a)
        downjQuery(a.get('href'), "css ")
        time.sleep (1)
        
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
    if not lockFile("css.lock.pid"):  
        sys.exit(0) 
    main ( )
    

