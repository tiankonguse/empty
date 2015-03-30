# python 基本类型


## None 

None 表示该值不存在,比如 没有定义返回值 的函数就 返回None  

相当于 javascript 中的 undefine.  


## True False

布尔类型,Ture等价于1,False等价于0  


## List

list 可以理解为 c语言中的数组，不过和javascript 的数组更类似点。  

```
test=[1,2,"yes"]
```

python 内置一些函数可以操作数组。  

### list 内建函数

append(x) 追加到链尾  

```
test.append(1) #追加到链尾

[1, 2, 'yes', 1]
```

extend(L) 追加一个列表,等价于+=  

```
test.extend([ 'no','maybe']) #追加一个列表  

[1, 2, 'yes', 1, 'no', 'maybe']
```

insert(i,x) 在位置i插入x  

```
test.insert(0,'never') #在位置0插入'never'

['never', 1, 2, 'yes', 1, 'no', 'maybe']
```

remove(x) 删除第一个值为x的元素,如果不存在会抛出异常  

```
test.remove('no') #删除第一个值为"no"的元素,如果不存在会抛出异常  

['never', 1, 2, 'yes', 1, 'maybe']
```

reverse() 反转序列  

```
test.reverse() #反转序列  

['maybe', 1, 'yes', 2, 1, 'never']
```

pop(\[i]) 返回并删除位置为i的元素,i默认为最后一个元素(i两边的\[]表示i为可选的,实际不用输入)  

```
test.pop() #返回并删除位置为i的元素,i默认为最后一个元素  

['maybe', 1, 'yes', 2, 1]
```

index(x) 返回第一个值为x的元素,不存在则抛出异常  

```
test.index('yes') #返回第一个值为'yes'的元素,不存在则抛出异常  

2
```

count(x) 返回x出现的次数  

```
test.count(1) #返回1出现的次数

2
```

sort() 排序  

```
test.sort() #排序  

[1, 1, 2, 'maybe', 'yes']
```

## list 切片

可以把切片理解为按一定规则提取数组的值吧。  

```
test=['never', 1, 2, 'yes', 1, 'no', 'maybe']

test[0:3] #包括test[0],不包括test[3]
['never', 1, 2]


test[0:6:2] #包括test[0],不包括test[6],而且步长为2
['never', 2, 1]


test[:-1] #包括开始,不包括最后一个
['never', 1, 2, 'yes', 1, 'no']

test[-3:] #抽取最后3个
[1, 'no', 'maybe']

test[::-1] #倒序排列
['maybe', 'no', 1, 'yes', 2, 1, 'never']
```

## list 推导

我们需要把循环生成值组装成一个数组时，可以使用推导写出简洁的代码来。  

```
freshfruit=['  banana  ','   loganberry  ']
ret = [weapon.strip() for weapon in freshfruit]

['banana', 'loganberry']
```

当然，我们也可以使用循环自己来实现

```
ret = []
for weapon in freshfruit:
    ret.append(weapon.strip())

['banana', 'loganberry']
```
但是你再看看下面的几个例子，就会发现推导的简洁性。  


满足条件的，并做一些简单的运算后生成数组。  

```
vec=[2,4,6]
[3*x for x in vec if x>3]

[12, 18]
```

双层循环

```
vec2=[4,3,-9]
[x*y for x in vec for y in vec2]

[8, 6, -18, 16, 12, -36, 24, 18, -54]

[vec[i]+vec2[i] for i in range(len(vec))]
[6, 7, -3]
```

快速遍历数字

```
[for i in range(1,6)]
```


