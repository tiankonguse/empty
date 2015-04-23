# Liquid 中的真与假

在编程语言的`if`语句中，我们分别使用`truthy`和`falsy`来表示条件返回的`true`和`false`.  

## truthy 是什么

在 Liquid 里面，不是`nil`和`false`的值都是`truthy`.  

在下面的例子中，文本`Tobi`不是 boolean 类型，　但是它在条件语句中是 `truthy`.  

```
{% assign tobi = 'Tobi' %}
{% if tobi %}
This will always be true.
{% endif %}
```

字符串即使是空的，它也是`truthy`.  
如果`settings.fp_heading`是空的话，下面的例子将会返回空的HTML标签．  

```
{% if settings.fp_heading %}
<h1>{{ settings.fp_heading }}</h1>
{% endif %}
```

将会输出  

```
<h1></h1>
```

为了避免这种情况，你应该检查字符串是否为空.  

```
{% unless settings.fp_heading == blank %}
    <h1>{{ settings.fp_heading }}</h1>
{% endunless %}
```

对于`EmptyDrop`也是`truthy`.  
下面的例子中，如果`settings.page`是空字符串，或者被设置为不可见，或者对象不存在，将会返回`EmptyDrop`值．  
结果将是不希望遇到的空的`<div>`.  

```
{% if pages[settings.page] %}
<div>{{ pages[settings.page].content }}</div>
{% endif %}
```

将会输出  

```
<div></div>
```

## falsy 是什么  

在Liquid 中，只有`nil`和`false`是`falsy`的．  
当Liquid对象没有东西返回的时候，将会返回`nil`.  
例如当`collection`不包含`image`时，`collection.image`将会返回`nil`,也就是`falsy`.  

```
{% if collection.image %}
<!-- output collection image -->
{% endif %}
```

值`false`被很多Liquid对象的属性返回,比如`product.available`.  

## 总结

简单的说，只有`false`和`nil`是`falsy`的．  



