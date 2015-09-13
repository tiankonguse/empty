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


def main ( ):

    print Rs_hash("1178555235")%10
   
#end main

    
if __name__ == "__main__":
    main ( )

