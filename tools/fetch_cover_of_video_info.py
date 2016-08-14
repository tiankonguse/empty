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

import json

import time

import datetime
import logging



debug = 1

reload(sys)

sys.setdefaultencoding('utf8')

today = datetime.date.today()

logfilepath = "./log/" + os.path.splitext(os.path.basename(__file__))[0] + "_" + today.strftime('%Y%m%d') + ".log"

logging.basicConfig(filename=logfilepath, level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s: %(message)s')


if debug :
    cover_dbcfg = {'host' : '10.12.191.99', 'port' : 3306, 'user' : 'user_qqlive', 'passwd' : 'qqlive', 'db' : 'd_v_idx'}
else:
    cover_dbcfg = {'host' : '10.189.30.54', 'port' : 3311, 'user' : 'root', 'passwd' : 'asdf1234', 'db' : 'd_v_idx'}


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


def fetchDict(cid, infodict): 
    """
        得到 所有符合条件的vid
    """
    try:
        
        dbcfg=cover_dbcfg
        conn = MySQLdb.connect(host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor()
        
        sql = ("SELECT c_vids FROM d_v_idx.t_cover_video_new where c_cid='%s' limit 1;" % (cid))
        cur.execute(sql)
        
        results = cur.fetchall()
        conn.close(); 
        
        for x in results:
            strVid = x[0]
            vidList = strVid.split('+')
            for vid in vidList:
                if len(vid) == 0:
                    continue
                infodict.append({"vid":vid,"title":""})
    except MySQLdb.Error, e:
        print ("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error("Mysql Error %d: %s" % (e.args[0], e.args[1]))
# end fetchCoverDict

def fetchInfo(infodict):
    """
        由 cid  查询对应的豆瓣id和时光id.
        条件：
            c_field_id in (342, 385) 对应(豆瓣, 时光)
            c_field_text 豆瓣和时光的id值
    """
    try:
        dbcfg=cover_dbcfg
        conn = MySQLdb.connect(host=dbcfg["host"], user=dbcfg["user"], passwd=dbcfg["passwd"], db=dbcfg["db"], port=dbcfg["port"], charset='utf8')
        cur = conn.cursor()
        
        for info in infodict:
            vid = info["vid"]
            x = (ord(vid[0]) - ord('0'))%10
            sql = ("SELECT c_title FROM d_v_idx.t_video_comm_%d where c_vid='%s' limit 1;" % (x, vid))
            cur.execute(sql)
            results = cur.fetchall()
            for x in results:
                info["title"] = x[0]
        conn.close()
    except MySQLdb.Error, e:
        print ("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        logging.error("Mysql Error %d: %s" % (e.args[0], e.args[1]))
#end fetchCoverDoubanTime

def saveInfo(infodict):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    filePath = ("vid_title_%s.json" % (today.replace("-","")))
    try:
        f = open(filePath, 'w')
        
        for info in infodict:
            # vid   title
            f.write("%s\t%s\n"%(info["vid"], info["title"]))
        print ("finish output. file : %s " % (filePath))
        f.close()
    except IOError, e:
        logging.error("Error %d: %s" % (e.args[0], e.args[1]))
#end saveInfo


def main():
    infodict = []
    cid = "fv5yce1z791diy3"
    print "fetchDict begin ",time.asctime( time.localtime(time.time()) )
    fetchDict(cid, infodict)
    print "fetchDict size=",len(infodict)
    
    print "fetchInfo begin ",time.asctime( time.localtime(time.time()) )
    fetchInfo(infodict)
    
    #infodict = sorted(infodict,key = lambda x:x['title']) 
    
    print "saveInfo begin ",time.asctime( time.localtime(time.time()) )
    saveInfo(infodict)
    
    
    print "end", time.asctime( time.localtime(time.time()) )
    

if __name__ == "__main__": 
    main()
    
