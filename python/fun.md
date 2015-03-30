# python 函数

## 函数定义  

```
def fib(n=2,a=1):#参数可以有默认值
    """这里给函数写文档注释"""
    for i in range(n):
        print a

f=fib #可以用一个变量表示函数
f(3)
# 1
# 1
# 1

fib(a=2) #多个可选参数赋值可以直接写"参数变量名＝值"来快速赋值
# 2
# 2
```

## Lambda函数

一种无名函数的速写法  

```
def make_incrementor(n):
    return lambda x: x+n

f=make_incrementor(n)
#f等价于
#def f(x):
#   return x+n
```


##　变参


参数格式为 \*para 表示接受一个元组  

为 \*\*para 表示接受一个字典  

\*para要在\*\*para之前  


```
def test(*args,**dic):
    for arg in args :
        print arg
    for k,v in dic.iteritems():
        print k ,':',v

test("yes",1,2,me="张沈鹏",where="中国") #"yes",1,2传递给元组;me="张沈鹏",where="中国"传递给字典

# yes
# 1
# 2
# me : 张沈鹏
# where : 中国
```

## 装饰器

```
@A 
def B:pass 
```

等价于 

```
def B:
    pass 
    B=A(B) 
```


即将函数B作为参数传给参数A  

```
from time import time
#测试运行时间
def cost_time(func):
    def result(*args,**dic):
        beign=time()
        func(*args,**dic)
        print "cost time : ",time()-beign
    return result

@cost_time
def show(n):
    for x in range(n):print x

show(10)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# cost time :  0.0469999313354
```

## 生成器表达式

生成器表达式:类似于没有中括号的列表推导式,可用在参数中  


```
sum(i*i for i in range(10))

unique_words=set(word for line in page for word in line.split())#page为打开的文件

data='golf'
list(data[i] for i in range(len (data)-1,-1,-1))
# ['f','l','o','g']
```

## yield

每次调用返回一个值,并记录当前执行位置所有的变量  

```
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

for char in reverse("golf"):
    print char,

# f l o g
```


