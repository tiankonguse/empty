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
下面的例子展示了`fulfillment`没有`tracking_numbers`成员的情况．  
`if`语句不会渲染它包含的内容.  

```
{% if fulfillment.tracking_numbers %}
We have a tracking number!
{% endif %}
```

任何的标签和输出的`nil`都不会在渲染结果中显示．  

```
Tracking number: {{ fulfillment.tracking_numbers }}
```

输入如下  

```
Tracking number: 
```

## Arrays

数组是一个所有类型的变量列表．  

### 访问数组的所有元素

为了访问数组的元素，你可以使用`for`或`tablerow`标签在数组里循环遍历每一个元素．  

```
<!-- if product.tags = "sale", "summer", "spring", "wholesale" -->
{% for tag in product.tags %}
    {{ tag }}
{% endfor %}
```


将会输出如下  

```
sale summer spring wholesale
```

### 访问数组指定的元素


你可以使用方括号`[]`来访问数组里指定的元素．  
数组的下标以`0`开始.  


```
<!-- if product.tags = "sale", "summer", "spring", "wholesale" -->
{{ product.tags[0] }} 
{{ product.tags[1] }} 
{{ product.tags[2] }} 
{{ product.tags[3] }} 
```

将会输出如下  

```
sale
summer
spring
wholesale
```

### 数组初始化

在 Liquid 中不能初始化数组．  
在 Javascript 中可以像下面的方式初始化数组  

```
<script>
var cars = ["Saab", "Volvo", "BMW"];
</script>
```

在Liquid里，你必须使用`split`过滤器将一个单独的字符串分割成子串数组.  


## EmptyDrop

当你通过 [handle][] 访问不存在的对象时，就会返回一个 EmptyDrop 对象.  
下面的　`page_1`, `page_2`, `page_3`都是　EmptyDrop 对象．  

```
{% assign variable = "hello" %}
{% assign page_1 = pages[variable] %}
{% assign page_2 = pages["i-do-not-exist-in-your-store"] %}
{% assign page_3 = pages.this-handle-does-not-belong-to-any-page %}
```

EmptyDrop 对象质包含一个只会返回`true`的`empty?`属性．  

Collections 和 pages 没有 `empty?` 属性, 在`if`语句中调用它，会返回`false`.  
当时用`unless`语句时，如果属性存在，则会返回`true`.  


### 应用在主题中

`empty?` 用于在使用一个属性前检查这个属性是否存在．  

```
{% unless pages.frontpage.empty? %}
  <!-- We have a page with handle 'frontpage' and it's not hidden.-->
  <h1>{{ pages.frontpage.title }}</h1>
  <div>{{ pages.frontpage.content }}</div>
{% endunless %}
```

为了避免在页面上输出空的HTML,先去检查一个页面是否存在是很重要的．  

不然就会像下面的样子  

```
<h1></h1>
<div></div>
```

你也可以对`collections`进行同样的验证．  

```
{% unless collections.frontpage.empty? %}
  {% for product in collections.frontpage.products %}
    {% include 'product-grid-item' %}
  {% else %}
    <p>We do have a 'frontpage' collection but it's empty.</p>
  {% endfor %}
{% endunless %}
```


[handle]: handle.md
