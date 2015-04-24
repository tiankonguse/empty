# 控制标签

控制标签就是条件分支标签。  

## if

`if`用于条件分支，条件为真时，执行内部的语句。  

```
{% if product.title == 'Awesome Shoes' %}
    These shoes are awesome!
{% endif %}
```

输出如下  

```
These shoes are awesome!
```


## elsif / else

`elsif`和`else`用于有多个条件分支的时候。  

```
 <!-- If customer.name = 'anonymous' -->
  {% if customer.name == 'kevin' %}
    Hey Kevin!
  {% elsif customer.name == 'anonymous' %}
    Hey Anonymous!
  {% else %}
    Hi Stranger!
  {% endif %}
```

输出如下  

```
Hey Anonymous!
```


## case/when

`case`的功能就和C语言中有`switch`功能类似。  

```
switch => case
case   => when 
default => else
```

不同之处是这个不需要加`break`语句。  

```
{% assign handle = 'cake' %}
{% case handle %}
  {% when 'cake' %}
     This is a cake
  {% when 'cookie' %}
     This is a cookie
  {% else %}
     This is not a cake nor a cookie
{% endcase %}
```

输出如下  


```
This is a cake
```


## unless

`unless`就是条件语句中的非。  
比如是c等语言中的`!`或者python语言中的`not`.  

```
  {% unless product.title == 'Awesome Shoes' %}
    These shoes are not awesome.
  {% endunless %}
```

输出如下  

```
These shoes are not awesome.
```

下面的语句和`unless`语句等价。  

```
 {% if product.title != 'Awesome Shoes' %}
    These shoes are not awesome.
  {% endif %}
```


