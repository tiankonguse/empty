# 操作简介

Liquid 可以使用所有的逻辑运算和比较运算。  
这个可以在`if`和`unless`标签中使用。  

## 基础操作

* `==` 相等
* `!=` 不等 
* `>`  大于
* `<` 小于 
* `>=` 大于等于 
* `<=` 小于等于 
* `or` 只要一个成立 
* `and` 所有都成立 

例如  

```
{% if product.title == "Awesome Shoes" %}
    These shoes are awesome!
{% endif %}
```

操作符可以连接在一起  

```
{% if product.type == "Shirt" or product.type == "Shoes" %}
    This is a shirt or a shoe. 
{% endif %}
```

## contains 操作符 

`contains` 用于检查一个串是否是另一个串的子串。  

```
{% if product.title contains 'Pack' %}
  This product's title contains the word Pack.
{% endif %}
```

`contains`还用来检查一个串是否在一个字符串数组中。  

```
{% if product.tags contains 'Hello' %}
  This product has been tagged with 'Hello'.
{% endif %}
```

`contains` 不支持检查一个串是否是在数组对象中(肯定不能检查啦)。  

下面的将不会生效。  

```
{% if product.collections contains 'Sale' %}
  One of the collections this product belongs to is the Sale collection.
{% endif %}
```

但是我们可以这样做。  

```
{% assign in_sale_collection = false %}
{% for collection in product.collections %}
  {% if in_sale_collection == false and collection.title == 'Sale' %}
    {% assign in_sale_collection = true %}
  {% endif %}
{% endfor %}
{% if in_sale_collection %}
  One of the collections this product belongs to is the Sale collection.
{% endif %}
```


