# python 字段 dict

典:关键字为不可变类型,如字符串,整数,只包含不可变对象的元组.  

列表等不可以作为关键字.  

如果列表中存在关键字对,可以用dict()直接构造字典.而这样的列表对通常是由列表推导式生成的.  


```
tel={'jack':4098,'sape':4139} 

tel['guido']=4127

# {'sape': 4139, 'jack': 4098, 'guido': 4127}

tel['jack'] #如果jack不存在,会抛出KeyError
# 4098

a.get("zsp",5000) #如果"zsp"为tel的键则返回其值,否则返回5000
# 5000

del tel['sape'] #删除键'sape'和其对应的值

tel.keys() #复制一份键的副本,同理tel.items()为值的副本
# ['jack', 'guido']

"jack" in tel #判断"jack"是否tel的键
# True

"zsp" not in tel
# True

for k,v in tel.iteritems():print k,v  #同理tel.iterkeys()为键的迭代器,tel.itervalues()为值的迭代器
# jack 4098
# guido 4127

tel.copy() #复制一份tel
# {'jack': 4098, 'guido': 4127}


tel.fromkeys([1,2],0) #从序列生成并返回一个字典,其值为第二个参数(默认为None),不改变当前字典
# {1: 0, 2: 0}

tel.popitem() #弹出一项
# ('jack', 4098)
```

