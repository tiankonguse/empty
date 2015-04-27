# 变量标签

变量标签主要用来创建新的标签。  

## assign

`assign`创建一个变量。  

```
 {% assign my_variable = false %}
  {% if my_variable != true %}
  This statement is valid.
  {% endif %}
```

输出如下  

```
This statement is valid.
```

字符串需要使用双引号引起来。  

```
{% assign foo = "bar" %}
{{ foo }}
```

输出如下  

```
bar
```

## capture

`capture`可以得到一个闭合标签内的值。  
`capture`创建的变量的值是字符串类型。  


```
{% capture my_variable %}I am being captured.{% endcapture %}
{{ my_variable }}
```

输出如下  

```
I am being captured.
```

## increment

创建一个数字变量，没调用一次，值增加1.初始值是0.  


```
{% increment variable %}
{% increment variable %}
{% increment variable %}
```

输出如下  

```
0
1
2
```

通过`increment`创建的变量与通过`assign`和`capture`创建的变量没有关系。  


```
{% assign var = 10 %}
{% increment var %}
{% increment var %}
{% increment var %}
{{ var }}
```
输出如下  

```
0
1
2
10 
```

## decrement

创建一个递减的数字变量，初始值是`-1`.  

```
{% decrement variable %}
{% decrement variable %}
{% decrement variable %}
```

输出如下  

```
-1
-2
-3
```


