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
    'Host':'redisdoc.com',
    'X-Forwarde-For':'195.154.92.79',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-language' : 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    'Upgrade-Insecure-Requests' : '1',
    'Referer' : 'http://redisdoc.com/index.html',
    'cookie': '_ga=GA1.2.1484608501.1444552427; _gat=1'
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


HOME_URL = "http://redisdoc.com/"


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
        info["content"] = urllib2.urlopen ( req,  timeout=5).read()

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
    nameList = name.split('/')
    if len(nameList) != 2:
        print "ERROR split name=%s " % name
        return 1
    redisDir = nameList[0]
    
    filePath = ("../data/%s" % (redisDir))
    
    os.system("mkdir -p %s" % filePath)
    
    filePath = ("../data/%s" % (name))
    try:
        f = open(filePath, 'w')
        f.write("---\n")
        f.write("layout: redis\n")
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
        
def downRedis(link, pre):
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
    content = soup.findAll("div",{"class" : "body"})
    
    
    soupContent = BeautifulSoup(str(content))
    
    if len(soupContent) == 0:
        print "soupContent is empty"
        return
        
    content = soupContent.findAll("div",{"class" : "section"})
    
    strContent = str(content[0])
    
    #related
    related = soup.findAll("div",{"class" : "related"}, limit=1)
    
    strContent = str(related[0]) + strContent
    
    #title
    
    
    title = soup.findAll("title")
    
    if (not title) or len(title) == 0:
        title = link
    else:
        title = title[0].string
        
    title = pre + title
    
    #description
    description = title
    
    #keywords
    keywords = title
    
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
    
    linkList = []
    
    # content
    aList = soup.findAll("a",{"class" : "reference"})

    for a in aList:
        if a in aMap:
            continue
        aMap.add(a)
        href = a.get('href')
        if href.find('http') != -1 :
            continue

        if href.find('change_log.html') != -1 :
            continue
            
        if href.find('#') != -1 :
            continue
            
        downRedis(href, "redis ")
        time.sleep (1)
        #break
        
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
    if not lockFile(".lock.pid"):  
        sys.exit(0) 
    main ( )
    

