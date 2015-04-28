# 数组过滤器



## join

`join` 可以使用传递的字符参数把数组连接起来．  

```
{{ product.tags | join: ', ' }}
```

输出如下  


```
tag1, tag2, tag3
```


## first


返回数组的第一个元素．  

```
<!-- product.tags = "sale", "mens", "womens", "awesome" -->
{{ product.tags | first }}
```

输出如下  

```
sale
```

在 [标签](tags.md) 中，可以使用点操作符来使用`first`.  

```
{% if product.tags.first == "sale" %}
    This product is on sale!
{% endif %}
```



## last

返回数组的最后一个元素．  

```
<!-- product.tags = "sale", "mens", "womens", "awesome" -->
{{ product.tags | last }}
```

输出如下  

```
awesome
```

在 [标签](tags.md) 中，也可以使用点操作符来使用`last`.  

```
{% if product.tags.last == "sale"%}
    This product is on sale!
{% endif %}
```

在字符串中，使用`last`可以得到最后一个字符．  

```
<!-- product.title = "Awesome Shoes" -->
{{ product.title | last }}
```

输出如下  

```
s
```



## map

数组元素的属性作为参数，使用数组元素的值创建一个字符串．  

```
<!-- collection.title = "Spring", "Summer", "Fall", "Winter" -->
{% assign collection_titles = collections | map: 'title' %}
{{ collection_titles }}
```

输出如下  

```
SpringSummerFallWinter
```


## size

返回数组或者字符串的大小．  

```
{{ 'is this a 30 character string?' | size }}
```

输出如下  

```
30
```

`size`在 [标签](tags.md) 中可以使用点操作符．  

```
{% if collections.frontpage.products.size > 10 %}
    There are more than 10 products in this collection! 
{% endif %}
```


## sort


根据数组中元素指定的属性来对数组排序。  


```
{% assign products = collection.products | sort: 'price' %}
{% for product in products %}
    <h4>{{ product.title }}</h4>
{% endfor %}
```

排序是大小写敏感的。  

```
<!-- products = "a", "b", "A", "B" -->
{% assign products = collection.products | sort: 'title' %}
{% for product in products %}
   {{ product.title }}
{% endfor %}
```

输出如下  

```
A B a b
```




