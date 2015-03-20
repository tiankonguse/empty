#coding:utf-8
import re,os,shutil,sys
import urllib2,socket,cookielib
from threading import Thread,stack_size,Lock
from Queue import Queue
import time
from gzip import GzipFile
from StringIO import StringIO

class ContentEncodingProcessor(urllib2.BaseHandler):
  """A handler to add gzip capabilities to urllib2 requests """

  # add headers to requests
  def http_request(self, req):
    req.add_header("Accept-Encoding", "gzip, deflate")
    return req

  # decode
  def http_response(self, req, resp):
    old_resp = resp
    # gzip
    if resp.headers.get("content-encoding") == "gzip":
        gz = GzipFile(
                    fileobj=StringIO(resp.read()),
                    mode="r"
                  )
        resp = urllib2.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code)
        resp.msg = old_resp.msg
    # deflate
    if resp.headers.get("content-encoding") == "deflate":
        gz = StringIO( deflate(resp.read()) )
        resp = urllib2.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code)  # 'class to add info() and
        resp.msg = old_resp.msg
    return resp

# deflate support
import zlib
def deflate(data):   # zlib only provides the zlib compress format, not the deflate format;
  try:               # so on top of all there's this workaround:
    return zlib.decompress(data, -zlib.MAX_WBITS)
  except zlib.error:
    return zlib.decompress(data)

class Fetcher:
    '''
    html Fetcher

    basic usage
    -----------
    from fetcher import Fetcher
    f = Fetcher()
    f.get(url)

    post
    ----
    req = urllib2.Request(...)
    f.post(req)

    multi-thread
    ------------
    f = Fetcher(threads=10)
    for url in urls:
        f.push(url)
    while f.taskleft()
        url,html = f.pop()
        deal_with(url,html)
    '''
    def __init__(self,timeout=10,threads=None,stacksize=32768*16,loginfunc=None):
        #proxy_support = urllib2.ProxyHandler({'http':'http://localhost:3128'})
        cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        encoding_support = ContentEncodingProcessor()
        #self.opener = urllib2.build_opener(cookie_support,encoding_support,proxy_support,urllib2.HTTPHandler)
        self.opener = urllib2.build_opener(cookie_support,encoding_support,urllib2.HTTPHandler)
        self.req = urllib2.Request('http://www.hsbc.com')
        socket.setdefaulttimeout(timeout)
        self.q_req = Queue()
        self.q_ans = Queue()
        self.lock = Lock()
        self.running = 0
        if loginfunc:
            self.opener = loginfunc(self.opener)
        if threads:
            self.threads = threads
            stack_size(stacksize)
            for i in range(threads):
                t = Thread(target=self.threadget)
                t.setDaemon(True)
                t.start()

    def __del__(self):
        time.sleep(0.5)
        self.q_req.join()
        self.q_ans.join()

    def taskleft(self):
        return self.q_req.qsize()+self.q_ans.qsize()+self.running

    def push(self,req,repeat=3):
        if not self.threads:
            print 'no thread, return get instead'
            return get(req,repeat)
        self.q_req.put(req)

    def pop(self):
        try:
            data = self.q_ans.get(block=True,timeout=10)
            self.q_ans.task_done()
        except:
            data = ['','']
        return data

    def threadget(self):
        while True:
            req = self.q_req.get()
            with self.lock:
                self.running += 1
            ans = self.get(req)
            print 'got',req
            self.q_ans.put((req,ans))
            try:
                self.q_req.task_done()
            except:
                pass
            with self.lock:
                self.running -= 1
            time.sleep(0.1) # don't spam

    def proxyisworking(self):
        try:
            self.opener.open('http://www.hsbc.com').read(1024)
            return True
        except Exception , what:
            print what
            return False
    def get(self,req,repeat=3):
        '''
        http GET req and repeat 3 times if failed
        html text is returned when succeeded
        '' is returned when failed
        '''
        try:
            response = self.opener.open(req)
            data = response.read()
        except Exception , what:
            print what,req
            if repeat>0:
                return self.get(req,repeat-1)
            else:
                print 'GET Failed',req
                return ''
        return data

    def post(self,req,repeat=3):
        '''
        http POST req and repeat 3 times if failed
        html text/True is returned when succeeded
        False is returned when failed
        '''
        if not isinstance(req,urllib2.Request):
            print 'post method need urllib.Request as argument'
            return False
        else:
            r = self.get(req,repeat)
            if r:
                return r
            else:
                return True

class SiteCopyer:
    def __init__(self,url):
        self.baseurl = url
        self.home = self.baseurl.split('/')[2]
        self.f = Fetcher(threads=10)
        self.create_dir()

    def create_dir(self):
        try:
            shutil.rmtree(self.home)
        except Exception,what:
            print what
        try:
            os.mkdir(self.home)
            os.mkdir(self.home+'/media')
            os.mkdir(self.home+'/media/js')
            os.mkdir(self.home+'/media/css')
            os.mkdir(self.home+'/media/image')
        except Exception,what:
            print what

    def full_link(self,link,baseurl=None):
        if not baseurl:
            baseurl = self.baseurl
        if '?' in link:
            link = link.rsplit('?',1)[0]
        if not link.startswith('http://'):
            if link.startswith('/'):
                link = '/'.join(baseurl.split('/',3)[:3]) + link
            elif link.startswith('../'):
                while link.startswith('../'):
                    baseurl = baseurl.rsplit('/',2)[0]
                    link = link[3:]
                link = baseurl+'/'+link
            else:
                link = baseurl.rsplit('/',1)[0]+'/'+link
        return link

    def link_alias(self,link):
        link = self.full_link(link)
        name = link.rsplit('/',1)[1]
        if '.css' in name:
            name = name[:name.find('.css')+4]
            alias = '/media/css/'+name
        elif '.js' in name:
            name = name[:name.find('.js')+3]
            alias = '/media/js/'+name
        else:
            alias = '/media/image/'+name
        return alias

    def strip_link(self,link):
        if link and (link[0] in ['"',"'"]):
            link = link[1:]
        while link and (link[-1] in ['"',"'"]):
            link = link[:-1]
        while link.endswith('/'):
            link = link[:-1]
        if link and (link[0] not in ["<","'",'"']) and ('feed' not in link):
            return link
        else:
            return ''

    def copy(self):
        page = self.f.get(self.baseurl)
        links = re.compile(r'<link[^>]*href=(.*?)[ >]',re.I).findall(page)
        links.extend( re.compile(r'<script[^>]*src=(.*?)[ >]',re.I).findall(page) )
        links.extend( re.compile(r'<img[^>]*src=(.*?)[ >]',re.I).findall(page) )
        templinks = []
        for link in links:
            slink = self.strip_link(link)
            if slink:
                templinks.append(slink)
        links = templinks
        for link in set(links):
            page = page.replace(link,self.link_alias(link)[1:])
            self.f.push( self.full_link(link) )
        open(self.home+'/index.html','w').write(page)
        while self.f.taskleft():
            url,page = self.f.pop()
            if url.endswith('.css'):
                links = re.compile(r'url\([\'"]?(.*?)[\'"]?\)').findall(page)
                templinks = []
                for link in links:
                    slink = self.strip_link(link)
                    if slink:
                        templinks.append(slink)
                links = templinks
                for link in set(links):
                    self.f.push( self.full_link(link,url) )
                    page = page.replace(link,self.link_alias(link)[1:].replace("media",".."))
            print 'write to',self.home+self.link_alias(url)
            try:
                open(self.home+self.link_alias(url),'w').write(page)
            except Exception,what:
                print what

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        SiteCopyer(url).copy()
    else:
        print "Usage: python "+sys.argv[0]+" url"

