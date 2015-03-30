# python 基本语法

## if 语句

```
x=int(raw_input("Please enter an integer:"))#获取行输入

if x>0:
    print '正数'
elif x==0:
    print '零'
else:
    print '负数'
```

如果只有两个简单的条件时，也可以像下面那样来简洁的实现。  

```
print "good" if 8==number else "bad" #当满足if条件时返回"good",否则返回"bad"
```

## in 语法


in判断 一个数 是否在 一个集合(如:元组,列表等) 中  

```
if 'yes' in  ('y','ye','yes'):
    print  'ok'
```

## fon-in

python中没有类似C中的for循环,而是使用for...in来对集合中的每一个元素进行操作  

```
a=['cat','door','example']
for x in a:
    print x
```

>  
> 如果在循环内修改循环的对象，结果将会不确定。  
>  


## break continue

这个和 c 语言中的语法类似，一个结束循环，一个执行下一步循环。  

```
for i in range(10):
    if 2==i:continue #结束当前循环,进入下一步循环
    if 6==i:break #跳出循环
    print i
```

## pass

pass是空语句，是为了保持程序结构的完整性。  


```
if True:
    pass #什么也不做
```

## is

用来比较两个变量是否指向同一内存地址(也就是两个变量是否等价) 而 == 是用来比较两个变量是否逻辑相等  

```
a=[1,2]
b=[1,2]
>>> a is b
False
>>> a == b
True
```


## del

用于删除元素  

```
a=[1,2,3,4,5,6]

del a[0]
a
>>>[2,3,4,5,6]

del a[2:4]
a
>>>[2,3,6]

del a[:]
a
>>>[]

del a
a
#抛出异常
>>>NameError: name 'a' is not defined
```

## 异常

try ... except用于异常处理  

```
try:
    x=int(raw_input("请输入数字:"))
except ValueError: #可以同时捕获多个异常,写法如except(RuntimeError,ValueError):
    #当输入非数字时
    print"您输入不是数字"
except: #省略异常名,可以匹配所有异常,慎用
    pass
else:#当没有异常时
    print 'result=',result
finally:#和Java中类似。一般用于释放资源，如文件，网络连接。
   print 'finish'
```


raise用于抛出异常,可以为自定义的异常类  

惯例是以Error结尾的类，同类的异常一般派生自同一个基类(如Exception)  


```
class MyError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return reper(self.value)
```


基类异常可以匹配派生类异常  

```
try:
    raise Exception("spam","egg")
except Exception,inst:#inst为该异常类的实例,为可选项
    print type(inst) #异常的类型
    print inst
```




