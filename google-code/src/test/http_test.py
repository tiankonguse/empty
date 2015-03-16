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
#import socke

#def create_connection(address, timeout=None, source_address=None):
#    sock = socks.socksocket()
#    sock.connect(address)
#    return sock
#end create_connection
useragent = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
    'X-Forwarde-For':'127.0.0.1'
}

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 7070)
            
# patch the socket module
socket.socket = socks.socksocket
#socket.create_connection = create_connection

def myrand():
    return random.randint(1, 126)
#end myrand

def rand_ip():
    return ("127.%d.%d.%d`" % (myrand(), myrand(),myrand()))
#rand_ip

def socks_test(url):
    useragent['X-Forwarde-For'] = rand_ip()
    req = urllib2.Request(url, None, useragent)
    str_ret=urllib2.urlopen(req).read()
    print url
    print str_ret
#end socks_test

def test(url):
    try:
        proxy_handler = urllib2.ProxyHandler({"socks5" : '127.0.0.1:7070'})
        opener = urllib2.build_opener(proxy_handler)
        req = urllib2.Request(url)
        page = opener.open(req,timeout=5)
        ret_str = page.read()
        print url 
        print ret_str
    except urllib2.HTTPError, e:
        print('(%s)http request error code - %s.' % (url, e.code))
    except urllib2.URLError, e:
        print('(%s)http request error reason - %s.' % (url, e.reason))
    except Exception: 
        print('(%s)http request generic exception: %s.' % (url, traceback.format_exc()))
#end test


def main():
    #test("http://github.tiankonguse.com/")
    #test("https://code.google.com/")
    socks_test("https://code.google.com/")
#end main

if __name__ == "__main__": 
    main()
