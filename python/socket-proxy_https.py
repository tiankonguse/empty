def handle_connection(conn):
    # 从socket读取头
    req_headers = get_header(conn)
    # 更改HTTP头
    ## 要没有HTTP头的话。。。
    if req_headers is None:
        return
    method, version, scm, address, path, params, query, fragment = \
        parse_header(req_headers)
    if method == 'GET':
        do_GET(conn,
               req_headers,
               address,
               path,
               params,
               query,
               method,
               version)
    elif method == 'CONNECT':
        # 注意
        address = (path.split(':')[0], int(path.split(':')[1]))
        do_CONNECT(conn,
                   req_headers,
                   address)


def do_CONNECT(conn, req_headers, address):
    # 建立socket用以连接URL指定的机器
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # soc.settimeout(4)
    # 尝试连接
    try:
        soc.connect(address)
    except socket.error, arg:
        conn.sendall("/1.1" + str(arg[0]) + " Fail\r\n\r\n")
        conn.close()
        soc.close()
    else:  # 若连接成功
        conn.sendall('HTTP/1.1 200 Connection established\r\n\r\n')
        # 数据缓冲区
        # 读取浏览器给出的消息
        try:
            while True:
                # 从客户端读取数据，并转发给conn
                data = conn.recv(99999)
                soc.sendall(data)
                # 从服务器读取回复，转发回客户端
                data = soc.recv(999999)
                conn.sendall(data)
        except:
            conn.close()
            soc.close()


def do_GET(conn, req_headers, address, path, params, query, method, version):
    path = urlparse.urlunparse(("", "", path, params, query, ""))
    req_headers = " ".join([method, path, version]) + "\r\n" +\
        "\r\n".join(req_headers.split('\r\n')[1:])
    # 建立socket用以连接URL指定的机器
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # soc.settimeout(1)
    # 尝试连接
    try:
        soc.connect(address)
    except socket.error, arg:
        conn.sendall("HTTP/1.1" + str(arg[0]) + " Fail\r\n\r\n")
        conn.close()
        soc.close()
    else:  # 若连接成功
        # 把HTTP头中连接设置为中断
        # 如果不想让火狐卡在那里不继续加载的话
        if req_headers.find('Connection') >= 0:
            req_headers = req_headers.replace('keep-alive', 'close')
        else:
            req_headers += req_headers + 'Connection: close\r\n'
        # 发送形如`GET path/params/query HTTP/1.1`
        # 结束HTTP头
        req_headers += '\r\n'
        soc.sendall(req_headers)
        # 发送完毕, 接下来从soc读取服务器的回复
        # 建立个缓冲区
        data = ''
        while 1:
            try:
                buf = soc.recv(8129)
                data += buf
            except:
                buf = None
            finally:
                if not buf:
                    soc.close()
                    break
        # 转发给客户端
        conn.sendall(data)
        conn.close()
