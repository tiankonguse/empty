#   Python正则表达式的用法   
  
##   字符串替换   
  
  
  
###  1.替换所有匹配的子串   
  
用newstring替换subject中所有与正则表达式regex匹配的子串  
  
  
```  
result, number = re.subn(regex, newstring, subject)  
```  
  
  
  
  
###  2.替换所有匹配的子串（使用正则表达式对象）   
  
  
```  
reobj = re.compile(regex)  
result, number = reobj.subn(newstring, subject)  
```  
  
  
   
  
##  字符串拆分   
  
###  1.字符串拆分   
  
  
```  
result = re.split(regex, subject)  
```  
  
  
  
  
  
###  2.字符串拆分（使用正则表示式对象）   
  
  
```  
reobj = re.compile(regex)  
result = reobj.split(subject)  
```  
  
  
  
##  匹配   
  
下面列出Python正则表达式的几种匹配用法：  
  
###  1.测试正则表达式是否匹配字符串的全部或部分   
  
  
  
```  
regex=ur"..." #正则表达式  
if re.search(regex, subject):  
    do_something()  
else:  
    do_anotherthing()  
```  
  
  
  
  
###   2.测试正则表达式是否匹配整个字符串   
  
  
  
```  
regex=ur"...\Z" #正则表达式末尾以\Z结束  
if re.match(regex, subject):  
    do_something()  
else:  
    do_anotherthing()  
```  
  
  
  
  
###  3. 创建一个匹配对象，然后通过该对象获得匹配细节   
  
  
  
```  
regex=ur"..." #正则表达式  
match = re.search(regex, subject)  
if match:  
    # match start: match.start()  
    # match end (exclusive): match.end()  
    # matched text: match.group()  
    do_something()  
else:  
    do_anotherthing()  
```  
  
  
  
###  4.获取正则表达式所匹配的子串   
(Get the part of a string matched by the regex)  
  
  
```  
regex=ur"..." #正则表达式  
match = re.search(regex, subject)  
if match:  
    result = match.group()  
else:  
    result = ""  
```  
  
  
  
###  5. 获取捕获组所匹配的子串   
(Get the part of a string matched by a capturing group)  
  
  
```  
regex=ur"..." #正则表达式  
match = re.search(regex, subject)  
if match:  
    result = match.group(1)  
else:  
    result = ""  
```  
  
  
  
###  6. 获取有名组所匹配的子串   
(Get the part of a string matched by a named group)  
  
  
```  
regex=ur"..." #正则表达式  
match = re.search(regex, subject)  
if match:  
    result = match.group("groupname")  
else:  
    result = ""  
```  
  
  
  
###  7. 将字符串中所有匹配的子串放入数组中   
(Get an array of all regex matches in a string)  
  
  
```  
result = re.findall(regex, subject)  
```  
  
  
  
###  8.遍历所有匹配的子串   
(Iterate over all matches in a string)  
  
  
```  
for match in re.finditer(r"<(.*?)\s*.*?/\1>", subject)  
    # match start: match.start()  
    # match end (exclusive): match.end()  
    # matched text: match.group()  
```  
  
  
  
###  9.通过正则表达式字符串创建一个正则表达式对象   
(Create an object to use the same regex for many operations)  
  
  
```  
reobj = re.compile(regex)  
```  
  
  
  
###  10.用法１的正则表达式对象版本   
（use regex object for if/else branch whether (part of) a string can be matched）  
  
  
```  
reobj = re.compile(regex)  
if reobj.search(subject):  
    do_something()  
else:  
    do_anotherthing()  
```  
  
  
  
###  11.用法２的正则表达式对象版本   
（use regex object for if/else branch whether a string can be matched entirely）  
  
  
```  
reobj = re.compile(r"\Z")　＃正则表达式末尾以\Z 结束  
if reobj.match(subject):  
    do_something()  
else:  
    do_anotherthing()  
```  
  
  
  
  
###   12.创建一个正则表达式对象，然后通过该对象获得匹配细节   
（Create an object with details about how the regex object matches (part of) a string）  
  
  
```  
reobj = re.compile(regex)  
match = reobj.search(subject)  
if match:  
    # match start: match.start()  
    # match end (exclusive): match.end()  
    # matched text: match.group()  
    do_something()  
else:  
    do_anotherthing()  
```  
  
  
  
###  13.用正则表达式对象获取匹配子串   
（Use regex object to get the part of a string matched by the regex）  
  
  
```  
reobj = re.compile(regex)  
match = reobj.search(subject)  
if match:  
    result = match.group()  
else:  
    result = ""  
```  
  
  
  
###   14.用正则表达式对象获取捕获组所匹配的子串   
（Use regex object to get the part of a string matched by a capturing group）  
  
  
```  
reobj = re.compile(regex)  
match = reobj.search(subject)  
if match:  
    result = match.group(1)  
else:  
    result = ""  
```  
  
  
  
###   15.用正则表达式对象获取有名组所匹配的子串   
（Use regex object to get the part of a string matched by a named group）  
  
  
```  
reobj = re.compile(regex)  
match = reobj.search(subject)  
if match:  
    result = match.group("groupname")  
else:  
    result = ""  
```  
  
  
  
###  16.用正则表达式对象获取所有匹配子串并放入数组   
（Use regex object to get an array of all regex matches in a string）  
  
  
```  
reobj = re.compile(regex)  
result = reobj.findall(subject)  
```  
  
  
  
###  17.通过正则表达式对象遍历所有匹配子串   
（Use regex object to iterate over all matches in a string）  
  
  
```  
reobj = re.compile(regex)  
for match in reobj.finditer(subject):  
    # match start: match.start()  
    # match end (exclusive): match.end()  
    # matched text: match.group()  
```  
  
  
  
  
