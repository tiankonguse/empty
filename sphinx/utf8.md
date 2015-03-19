# utf8中文编码范围

UTF-8有点类似于Haffman编码，它将Unicode编码为：
00000000-0000007F的字符，用单个字节来表示；
00000080-000007FF的字符用两个字节表示 （中文的编码范围）
00000800-0000FFFF的字符用3字节表示

编码转换：iconv -f “文件目前编码” -t “文件转换后的编码” -o “转换后生成的新文件名” “源文件名”temp = Iconv.conv(“UTF-8″,“gb2312″,a)

因为目前为止Unicode-16规范没有指定FFFF以上的字符，所以UTF-8最多是使用3个字节来表示一个字符。但理论上来说，UTF-8最多需要用6字节表示一个字符。

在UTF-8里，英文字符仍然跟ASCII编码一样，因此原先的函数库可以继续使用。而中文的编码范围是在0080-07FF之间，因此是2个字节表示（但这两个字节和GB编码的两个字节是不同的）。

0、big endian和little endian
big endian和little
endian是CPU处理多字节数的不同方式。例如“汉”字的Unicode编码是6C49。那么写到文件里时，究竟是将6C写在前面，还是将49写在前面？如果将6C写在前面，就是big
endian。还是将49写在前面，就是little endian。

“endian”这个词出自《格列佛游记》。小人国的内战就源于吃鸡蛋时是究竟从大头(Big-Endian)敲开还是从小头(Little-Endian)敲开，由此曾发生过六次叛乱，其中一个皇帝送了命，另一个丢了王位。

我们一般将endian翻译成“字节序”，将big endian和little
endian称作“大尾”和“小尾”。

4、UTF编码

UTF-8就是以8位为单元对UCS进行编码。从UCS-2到UTF-8的编码方式如下：

UCS-2编码(16进制) UTF-8 字节流(二进制)
0000 – 007F 0xxxxxxx
0080 – 07FF 110xxxxx 10xxxxxx
0800 – FFFF 1110xxxx 10xxxxxx 10xxxxxx

例如“汉”字的Unicode编码是6C49。6C49在0800-FFFF之间，所以肯定要用3字节模板了：1110xxxx
10xxxxxx 10xxxxxx。将6C49写成二进制是：0110 110001 001001，
用这个比特流依次代替模板中的x，得到：11100110 10110001 10001001，即E6 B1 89。

读者可以用记事本测试一下我们的编码是否正确。

UTF-16以16位为单元对UCS进行编码。对于小于0×10000的UCS码，UTF-16编码就等于UCS码对应的16位无符号整数。对于不 小于 0×10000的UCS码，定义了一个算法。不过由于实际使用的UCS2，或者UCS4的BMP必然小于0×10000，所以就目前而言，可以认为 UTF-16和UCS-2基本相同。但UCS-2只是一个编码方案，UTF-16却要用于实际的传输，所以就不得不考虑字节序的问题。

5、UTF的字节序和BOM
UTF-8以字节为编码单元，没有字节序的问题。UTF-16以两个字节为编码单元，在解释一个UTF-16文本前，首先要弄清楚每个编码单元的字节序。 例如收到一个“奎”的Unicode编码是594E，“乙”的Unicode编码是4E59。如果我们收到UTF-16字节流“594E”，那么这是“奎 ”还是“乙”？

Unicode规范中推荐的标记字节顺序的方法是BOM。BOM不是“Bill Of
Material”的BOM表，而是Byte Order Mark。BOM是一个有点小聪明的想法：

在UCS编码中有一个叫做”ZERO WIDTH NO-BREAK
SPACE”的字符，它的编码是FEFF。而FFFE在UCS中是不存在的字符，所以不应该出现在实际传输中。UCS规范建议我们在传输字节流前，先传输字符”ZERO
WIDTH NO-BREAK SPACE”。

这样如果接收者收到FEFF，就表明这个字节流是Big-Endian的；如果收到FFFE，就表明这个字节流是Little-Endian的。因此字符”ZERO
WIDTH NO-BREAK SPACE”又被称作BOM。

UTF-8不需要BOM来表明字节顺序，但可以用BOM来表明编码方式。字符”ZERO
WIDTH NO-BREAK SPACE”的UTF-8编码是EF BB
BF（读者可以用我们前面介绍的编码方法验证一下）。所以如果接收者收到以EF BB
BF开头的字节流，就知道这是UTF-8编码了。

Windows就是使用BOM来标记文本文件的编码方式的。
