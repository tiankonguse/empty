# -*-coding:utf8-*-

# -*-coding:utf8-*-

import re, time, os
import urllib2, cookielib, urllib
from bs4 import BeautifulSoup as bs
import requests
import logging

delUid = '目标的人人uid'
delKeyword = u'目标的名字'
loginUrl = "http://3g.renren.com/login.do?autoLogin=true&&fx=0"
getLastStatusPageUrl = "http://3g.renren.com/status/getdoing.do?&sid=%s&id=%s&htf=35&sour=profile"
statusListUrl = "http://3g.renren.com/status/getdoing.do?curpage=%d&id=%s&sid=%s"
captchaPattern = "/><img src=\"(?P<url>http://captcha\.renren\.com/captcha\?post=.+?)\" alt=\""
sidPattern = r"sid=(?P<sid>.+?)\&"
uidPattern = r"http\://3g\.renren\.com/profile\.do\?id=(?P<uid>\d+?)\&"
statusPattern = r"\ </p><a href=\"(?P<url>.+?)\">回复\((?P<commentNumber>\d+?)\)"

def login(user, password, verifyCode=''):
    cookie = cookielib.CookieJar()
    cookieHandler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookieHandler)
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener.addheaders = [headers]

    newLogin = urllib2.Request(loginUrl)
    login = opener.open(newLogin)
    loginText = login.read().decode('utf-8')
    soup = bs(loginText)
    inputList = soup.findAll('input')
    lbsKey = inputList[1]['value']

    loginValues = {'origURL': '/home.do', 
        'lbskey': lbsKey,
        'c': '',
        'pq': '',
        'appid': '',
        'ref': 'http://m.renren.com/q.do?null',
        'email': user, 
        'password': password,
        'login': '登录'}
    postContent = urllib.urlencode(loginValues)
    req = urllib2.Request(loginUrl,postContent)
    login = opener.open(req)
    loginPage = login.read()
    if loginPage.find("#ffebe8") == -1:
        print str(user) + "登录成功"
        sids = re.search(sidPattern, loginPage)
        if sids:
            sid = sids.group('sid')
            print sid
        uids = re.search(uidPattern, loginPage)
        if uids:
            uid = uids.group('uid')
            print uid
    else:
        print "登录失败"
        else:
            raise SystemExit(1)
    return {'opener': opener, 'sid':sid, 'uid': uid}

def getLastStatusPageNumber(info):
    opener = info['opener']
    req = urllib2.Request(getLastStatusPageUrl % (info['sid'], info['uid']))
    result = opener.open(req)
    resultPage = result.read()
    pat = r"\(第1/(?P<last>\d+?)页\)"
    lasts = re.search(pat,resultPage)
    return int(lasts.group('last'))

def getStatusList(i, info):
    print "当前页码：" + str(i)
    opener = info['opener']
    req = urllib2.Request(statusListUrl % (i, info['uid'], info['sid']))
    result = opener.open(req)
    resultPage = result.read()
    pat = re.compile(statusPattern)
    statusList = pat.findall(resultPage)
    return statusList

def filterComment(url, info, j):
    opener = info['opener']
    req = urllib2.Request(url)
    result = opener.open(req)
    resultPage = result.read()
    soup = bs(resultPage.decode('utf-8'))
    status = soup.findAll('div', attrs={'class': 'sec'})[2].text
    print status
    logging.debug(status + " PageNo. " + str(j + 1))
    commentsList = soup.findAll('div', {'class': ''}, id='')
    for c in commentsList:
        r = delByUid(c, info)
        if not r:
            delByKeyword(c, info)

def delByUid(c, info):
    result = c.find(attrs={'href': re.compile(r'http://3g\.renren\.com/profile\.do\?id=' + delUid)})
    if result:
        print c.text.encode('utf-8')
        logging.debug(c.text.encode('utf-8'))
        delete = c.find('a', attrs={'href': re.compile(r'http://3g\.renren.com/status/wdelstatusreply\.do')})
        delPageUrl = delete.attrs['href']
        delComment(delPageUrl, info)

def delByKeyword(c, info):
    result = c.text.find(delKeyword)
    if result > -1:
        print c.text.encode('utf-8')
        logging.debug(c.text.encode('utf-8'))
        delete = c.find('a', attrs={'href': re.compile(r'http://3g\.renren.com/status/wdelstatusreply\.do')})
        delPageUrl = delete.attrs['href']
        delComment(delPageUrl, info)

def delComment(url, info):
    opener = info['opener']
    req = urllib2.Request(url)
    result = opener.open(req)
    resultPage = result.read()
    soup = bs(resultPage.decode('utf-8'))
    postUrl = soup.find('form')
    postValues = {}
    if postUrl:
        postUrl = postUrl.attrs['action']
        inputs = soup.findAll('input')
        for i in inputs:
            postValues[i.attrs['name']] = i.attrs['value']
        postValues['publish'] = postValues['publish'].encode('utf-8')
        postContent = urllib.urlencode(postValues)
        req = urllib2.Request(postUrl, postContent)
        delResult = opener.open(req)
        delResultPage = delResult.read()
        if delResultPage.find('删除评论成功'):
            print '删除该评论成功'
        else:
            raise SystemExit(1)
    else:
        raise SystemExit(1)

def main():
    logging.basicConfig(filename = os.path.join(os.getcwd(), 'dellog.txt'), level = logging.DEBUG)
    info = login('登录账号', '密码')
    lastStatusPage = getLastStatusPageNumber(info)
    for i in xrange(63, lastStatusPage):
        logging.debug('当前状态页码' + str(i))
        statusList = getStatusList(i, info)
        if statusList and statusList != [()]:
            for item in statusList:
                j = int(item[1]) / 10 + 1
                for curpage in xrange(0, j):
                    print curpage
                    url = item[0].replace("&", "&") + "&curpage=" + str(curpage)
                    filterComment(url, info, curpage)

if __name__ == '__main__':
    main()
