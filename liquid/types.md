# 类型

Liquid 对象可以返回下面六种类型：String, Number, Boolean, Nil, Array, or EmptyDrop  
Liquid 变量可以使用`assign`和`capture`标签初始化  

## String

声明变量时，可以用过`'`和`"`包含字符串。  

```
{% assign my_string = "Hello World!" %}
```

## Number

数字包含浮点数和整数。  

```
{% assign my_num = 25 %}
```

## Boolean

Booleans 是真或者假。  
声明一个 Boolean 类型时不需要加引号。  

```
{% assign foo = true %}
{% assign bar = false %}
```

## Nil

当 Liquid 没有结果时，返回的空值就是 Nil.  
它不是包含引号的`"nil"`  

在`{% if %}`和其他检查真假的标签中，Nil 被认为是 `false`.  
下面的例子展示了``


