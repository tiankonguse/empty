#coding:utf-8
import BaseHTTPServer
import select
import socket
import SocketServer
import urlparse
import httplib
import StringIO
import sys
import os
# 多线程HTTPServer
class ThreadingHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer): 
    pass

class ProxyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    __base = BaseHTTPServer.BaseHTTPRequestHandler
    __base_handle = __base.handle
    server_version = "HTTPProxy"
    # handle() is be calling in a new thread when a client is connected.
    def handle(self): 
        print 'handle()'
        self.__base_handle()
        return 

    def do_CONNECT(self):
        print 'do_CONNECT()'
        # HTTP Protocol CONNECT command
        self.log_request(200)
        self.wfile.write(self.protocol_version + " 200 Connection established\r\n")
        self.wfile.write("Proxy-agent: %s\r\n" % self.version_string())
        self.wfile.write("\r\n")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host, port = self.path.split(':')
        port = int(port)
        s.connect((host, port))
        self.turn_to(s, 900)
        s.close()
        self.connection.close()
        print 'a client is disconnected'

    # the most process in do_GET function
    def do_GET(self):
        print 'do_GET()'
        #netloc is a url like 'www.codepongo.com:80'
        (scheme, netloc, path, params, query, fragment) = urlparse.urlparse(self.path, 'http')
        if not netloc:
            netloc = self.headers.get('Host', "")
        if scheme != 'http' or not netloc or fragment:
            self.send_error(400, "bad url %s" % self.path)
            return
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if -1 != netloc.find(':'):
            host, port = netloc.split(':')
            port = int(port)
        else:
            host = netloc
            port = 80
        print host, port
        s.connect((host, port))
        self.log_request()
        # send HTTP Request HEADER
        s.send("%s %s %s\r\n" % (self.command, urlparse.urlunparse(('', '', path, params, query, '')), self.request_version))
        self.headers['Connection'] = 'close'
        del self.headers['Proxy-Connection']
        for key_val in self.headers.items():
            s.send("%s: %s\r\n" % key_val)
        s.send("\r\n")
        self.turn_to(s)
        s.close()
        self.connection.close()    
        print 'a client is disconnected'

    do_HEAD = do_GET
    do_POST = do_GET
    do_PUT  = do_GET
    do_DELETE=do_GET

    def turn_to(self, s, timeout = 60):
        #  client <-self.connection-> proxy <-s-> server
        # s 客户端与代理服务器的连接
        # self.connection 代理服务器与外部服务器之间的连接
        iw = [self.connection, s]
        ow = []
        time = 0
        while time < timeout:
            time += 1
            (ins, _, exs) = select.select(iw, ow, iw, 1)
            if exs: #exception
                for e in exs:
                    print "%s is exception" % (s.getpeername())
                break
            elif ins: #input readable
                for i in ins:
                    if i is s:
                        o = self.connection
                    elif i is self.connection:
                        o = s
                    else:
                        pass
                    data = i.recv(8192)
                    if data:                        
                        print 'recv length is', len(data)
                        o.send(data)
                        time = 0
                    else:
                        pass
            else: # output readable
                pass

def serving(port = 8000, protocol="HTTP/1.0", debug = False):
    host_port = ('', port)
    ThreadingHTTPServer.protocol_version = protocol
    httpd = ThreadingHTTPServer(host_port, ProxyHandler)
    print httpd.socket.getsockname()
    if not debug:
        buff = StringIO.StringIO()
        sys.stdout = buff
        sys.stderr = buff
    httpd.serve_forever()

if __name__ == '__main__':
    serving(port=8000, debug=True)
