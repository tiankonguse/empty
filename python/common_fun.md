# python 常用函数

## eval

对字符串参数运算,求值  

```
eval("1 + 2*3") #可以方便的用来做四则运算
# 7

a=1
eval('a+1') #可以访问变量
# 2
```


## exec

将字符串参数作为python脚本执行  

```
exec('a="Zsp"')  
# 'Zsp'
```


## execfile

和exec类似,不过是用来打开一个文件,并作为python脚本执行  

## dir

显示对象的所有属性(即可以用"."操作直接访问)  

```
dir([])

['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__str__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

## help

help(类/函数) 返回相应对象的文档字符串  

```
help(vars)

# Help on built-in function vars in module __builtin__:
# 
# vars(...)
#     vars([object]) -> dictionary
#     
#     Without arguments, equivalent to locals().
#     With an argument, equivalent to object.__dict__.
```

## len

返回序列/字典的长度

```
len([1,2,3])
# 3
```

## print

输出字符串 

```
print "Today ", #加逗号,输出后不换行

print "hello,%s!"%name #%s 表示用str转化为字符串
```

对于字典可以用变量名来直接格式化  

```
table={'Sjoerd':4127,'Jack':4098,'Dcab':8637678}

print 'Jack:%(Jack)d; Sjoerd:%(Sjoerd)d; Dcab:%(Dcab)d' % table

# Jack:4098; Sjoerd:4127; Dcab:8637678
```


同时,函数vars()返回包含所有变量的字典,配合使用,无坚不摧!  


##　raw_input

```
x=raw_input("Please enter an sentence:") #将输入的内容赋值给x
```


## range

```
range(10,0,-3)#参数的含义为起点(默认为0),终点(不含终点),步长(默认为1)
# [10,7,4,1]
```


## filter

filter(function , sequence) 返回序列,为原序列中能使function返回true的值  

```
a=[1,2,3,4]
filter(lambda x:x%2,a)
# [1, 3]
```


## map

`map(function,sequence,[sequence...])`返回序列,为对原序列每个元素分别调用function获得的值.  

可以传入多个序列,但function也要有相应多的参数  

```
map(lambda x,y,z:x+y+z,range(1,3),range(3,5),range(5,7))  

# 1+3+5=9
# 2+4+6=12
# [9,12]
```


## reduce



`reduce(function,sequence,[init])`返回一个单值为,计算步骤为  

* 第1个结果=function(sequence\[0],sequence\[1])
* 第2个结果=function(第1个结果,sequence\[2])
* 返回最后一个计算得值
* 如果有init,则先调用function(init,sequence\[0]) 
* sequence只有一个元素时,返回该元素,为空时抛出异常.


```
reduce(lambda x,y:x+y,range(3),99)
# 99+0=99 => 99+1=100 => 100+2=102
# 102
```


## zip

zip用于多个sequence的循环  

```
questions=['name','quest','favorite color']
answers=['lancelot','the holy grail','blue']

for q,a in zip(questions,answers):
    print 'What is your %s ? It is %s.'%(q,a)

# What is your name ? It is lancelot.
# What is your quest ? It is the holy grail.
# What is your favorite color ? It is blue.
```

## reversed

反向循环  

```
for i in reversed(range(1,4)):
    print i

# 3
# 2
# 1
```

## sorted

返回一个有序的新序列  

```
sorted([2,5,1,4])

# [1, 2, 4, 5]
```

## enumerate 

返回索引位置和对应的值  

```
for i,v in enumerate(['tic','tac','toe'])
    print i,v

# 0 tic
# 1 tac
# 2 toe
```



