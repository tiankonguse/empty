# 迭代标签

迭代标签用来重复的执行一些代码。  

> 注：如果你是程序员，使用几分钟快速浏览一下就可以了。  

## for

`for`就是一个能够让你循环执行一个代码的标签。  
在循环内能够使用的属性，请参考 [for loops][for-loops]  

`for`循环一页只能输出50个结果。  
如果你的数据超过50个，可以使用[paginate][theme-tags-paginate]标签来创建多页数据。  

> 注：for循环输出的个数实际上不受限制。  
> 可能文档上的意思是一页不建议输出很多结果来。  
> 比如我的[这个页面][github-map]上的很多链接里，都是`for`输出的，都上百个了。  


```
  {% for product in collection.products %}
      {{ product.title }}
  {% endfor %}
```

输出结果如下  

```
hat shirt pants
```

for的参数如下

### limit 

循环到达指定的下标时结束循环。  


```
 <!-- if array = [1,2,3,4,5,6] -->
  {% for item in array limit:2 %} 
    {{ item }}
  {% endfor %} 
```


输出结果如下  

```
1 2 
```

### offset

指定开始循环的下标。  

```
<!-- if array = [1,2,3,4,5,6] -->
  {% for item in array offset:2 %} 
    {{ item }} 
  {% endfor %} 
```

输出结果如下  

```
3 4 5 6
```

### range

定义一个区间数字，然后可以循环遍历。  
区间数组可以是变量，也可以是常数。  

```
{% assign num = 4 %}
{% for i in (1..num) %}
  {{ i }} 
{% endfor %}

{% for i in (3..5) %}
  {{ i }} 
{% endfor %}
```

输出结果如下  

```
1 2 3 4
3 4 5
```

### reversed

相反的顺序访问数组  

```
<!-- if array = [1,2,3,4,5,6] -->
{% for item in array reversed %} 
    {{ item }} 
{% endfor %} 
```

输出结果如下  

```
6 5 4 3 2 1
```

## cycle

循环访问一个字符串组合，每访问一次，下标后移一次，移到最后自动从头开始。  

```
{% cycle 'one', 'two', 'three' %}
{% cycle 'one', 'two', 'three' %}
{% cycle 'one', 'two', 'three' %}
{% cycle 'one', 'two', 'three' %} 
```

输出结果如下  

```
one
two
three
one
```

### 参数

由于一个字符串组合是循环迭代的，所以在表格中，有些行输出的个数不一致时，就会得到你不想要的结果。  

```

<ul>
{% for product in collections.collection-1.products %}
  <li{% cycle ' style="clear:both;"', '', '', ' class="last"' %}>
    <a href="{{ product.url | within: collection }}">
      <img src="{{ product.featured_image.src | product_img_url: 'medium' }}" alt="{{ product.featured_image.alt }}" />
    </a>
  </li>
{% endfor %}
</ul>
<ul>
{% for product in collections.collection-2.products %}
  <li{% cycle ' style="clear:both;"', '', '', ' class="last"' %}>
    <a href="{{ product.url | within: collection }}">
      <img src="{{ product.featured_image.src | product_img_url: 'medium' }}" alt="{{ product.featured_image.alt }}" />
    </a>
  </li>
{% endfor %}
</ul>
```


输出结果如下  

```
<ul>
  <li style="clear:both"></li>
</ul>
<ul>
  <li></li>
  <li class="last"></li>
  <li style="clear:both"></li>
  <li></li>
</ul>
```

有时候为了能并从新开始一个字符串组合， 我们可以给字符串组合一个别名。  

```
<ul>
{% for product in collections.collection-1.products %}
  <li{% cycle 'group1': ' style="clear:both;"', '', '', ' class="last"' %}>
    <a href="{{ product.url | within: collection }}">
      <img src="{{ product.featured_image.src | product_img_url: "medium" }}" alt="{{ product.featured_image.alt }}" />
    </a>
  </li>
{% endfor %}
</ul>
<ul>
{% for product in collections.collection-2.products %}
  <li{% cycle 'group2': ' style="clear:both;"', '', '', ' class="last"' %}>
    <a href="{{ product.url | within: collection }}">
      <img src="{{ product.featured_image.src | product_img_url: "medium" }}" alt="{{ product.featured_image.alt }}" />
    </a>
  </li>
{% endfor %}
</ul>
```

输出结果如下  

```
<ul>
  <li style="clear:both"></li>
  <li></li>
</ul>
<!-- new cycle group starts! -->
<ul>
  <li style="clear:both"></li>
  <li></li>
  <li></li>
  <li class="last"></li>
</ul>
```

## tablerow

tablerow 主要用于生成表格。  
首先必须在 `table` 标签内。  

关于`tablerow`的完整属性，请参考[tablerow][]


```
<table>
{% tablerow product in collection.products %}
  {{ product.title }}
{% endtablerow %}
</table>
```

输出结果如下  

```
<table>
    <tr class="row1">
        <td class="col1">
            Cool Shirt
        </td>
        <td class="col2">
            Alien Poster
        </td>
        <td class="col3">
            Batman Poster
        </td>
        <td class="col4">
            Bullseye Shirt
        </td>
        <td class="col5">
            Another Classic Vinyl
        </td>
        <td class="col6">
            Awesome Jeans
        </td>
    </tr>
</table>
```

参数如下  

### cols

指定表格有多少列。  

```
{% tablerow product in collection.products cols:2 %}
  {{ product.title }}
{% endtablerow %}
```

输出结果如下  

```
<table>
    <tr class="row1">
        <td class="col1">
            Cool Shirt
        </td>
        <td class="col2">
            Alien Poster
        </td>
    </tr>
    <tr class="row2">
        <td class="col1">
            Batman Poster
        </td>
        <td class="col2">
            Bullseye Shirt
        </td>
    </tr>
    <tr class="row3">
        <td class="col1">
            Another Classic Vinyl
        </td>
        <td class="col2">
            Awesome Jeans
        </td>
    </tr>
</table>    
```

### limit

输出数组的前几项。  

```
{% tablerow product in collection.products cols:2 limit:3 %}
  {{ product.title }}
{% endtablerow %}
```

### offset

从数组的第几项开始输出。  

```
{% tablerow product in collection.products cols:2 offset:3 %}
  {{ product.title }}
{% endtablerow %}
```

### range

可以遍历数字区间， 数字可以是常量，也可以是变量。  

```
<!--variable number example-->

{% assign num = 4 %}
<table>
{% tablerow i in (1..num) %}
  {{ i }} 
{% endtablerow %}
</table>

<!--literal number example-->

<table>
{% tablerow i in (3..5) %}
  {{ i }} 
{% endtablerow %}
</table>
```

[tablerow]: tablerow.md
[github-map]: http://github.tiankonguse.com/map
[for-loops]: for-loops.md 
