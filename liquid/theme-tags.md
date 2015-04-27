# 布局标签

布局标签有很多功能，如下  

* 输出html标签
* 决定使用哪个布局文件或代码片段
* 将返回结果集产分成多个页面

## 注释

注释可以让你在模板中加入不被渲染的内容。  
任何在`comment`区域内的文本都不会被执行，即使是Liquid 代码也不会被执行。  


```
 My name is {% comment %}super{% endcomment %} Shopify.
```

输出如下  

```
My name is Shopify.
```

## include

插入代码片段，代码片段的位置由布局配置决定。  


```
{% include 'snippet-name' %}
```

> 注意：上面的代码中，省略了后缀 `.liquid` 。  


当一个代码片段被引用后， 代码片段就可以使用引入它的那个模板内的变量。  

## 包含时指定变量


这里有两个方法在代码片段中引入变量。  

你可以先为变量赋值，然后再引入代码片段。  

```
{% assign snippet_variable = 'this is it' %}
{% assign snippet_variable_two = 'this is also it' %}
{% include 'snippet' %}
```

你也可以把他们写在一起。  


```
{% include 'snippet', snippet_variable: 'this is it', snippet_variable_two: 'this is also it' %}
```

### with

没啥用。  
`with`参数给代码片段里与代码片段同名的变量赋值。  

例如我们有一个名字是`color.liquid`代码片段。  

内容如下  

```
color: '{{ color }}'
shape: '{{ shape }}'
```

然后我们可以这样使用了  

```
{% assign shape = 'circle' %}
{% include 'color' %}
{% include 'color' with 'red' %}
{% include 'color' with 'blue' %}
{% assign shape = 'square' %}
{% include 'color' with 'red' %}
```


输出如下  

```
color: shape: 'circle'
color: 'red' shape: 'circle'
color: 'blue' shape: 'circle'
color: 'red' shape: 'square'
```


## 表单  

生成一个有各种属性的`<form>`元素和一个`<input>`标签用于提交表单。  


> 下面这些都没啥用吧。  


### activate_customer_password

使用[activate_customer_password][activate_customer_password.md]模板生成一个登陆的表单  


```
{% form 'activate_customer_password' %}
...
{% endform %}
```

输出如下  

```
<form accept-charset="UTF-8" action="https://my-shop.myshopify.com/account/activate" method="post">
    <input name="form_type" type="hidden" value="activate_customer_password" />
    <input name="utf8" type="hidden" value="✓" />
    ... 
</form>
```

### new_comment  

使用[article.liquid][article-liquid.md]模板生成一个评论表单。  
需要`article`对象作为参数。  


```
{% form "new_comment", article %}
...
{% endform %}
```

显示如下  

```
<form accept-charset="UTF-8" action="/blogs/news/10582441-my-article/comments" class="comment-form" id="article-10582441-comment-form" method="post">
    <input name="form_type" type="hidden" value="new_comment" />
    <input name="utf8" type="hidden" value="✓" />
    ...
</form>
```

### contact

使用`Liquid contact form`生成一个有邮箱输入框和提交按钮的表单。  

```
{% form 'contact' %}
...
{% endform %}
```

显示如下  

```
<form accept-charset="UTF-8" action="/contact" class="contact-form" method="post">
    <input name="form_type" type="hidden" value="contact" />
    <input name="utf8" type="hidden" value="✓" />
    ...
</form>
```

### create_customer

创建用户的表单。  


```
{% form 'create_customer' %}
...
{% endform %}
```

显示如下  

```
<form accept-charset="UTF-8" action="https://my-shop.myshopify.com/account" id="create_customer" method="post">
    <input name="form_type" type="hidden" value="create_customer" />
    <input name="utf8" type="hidden" value="✓" />
    ...
</form>
```

### customer_address

联系地址相关的表单。  


```
{% form 'customer_address', customer.new_address %}
...
{% endform %}
```

显示如下  


```
<form accept-charset="UTF-8" action="/account/addresses/70359392" id="address_form_70359392" method="post">
    <input name="form_type" type="hidden" value="customer_address" />
    <input name="utf8" type="hidden" value="✓" />
    ...
</form>
```

## layout

从布局目录中加载本地模板文件。  
如果没有找到模板文件，则加载默认的`theme.liquid`模板文件。  

```
<!-- loads the templates/alternate.liquid template -->
{% layout 'alternate' %}
```

如果你不想加载任何模板，可以使用`none`.  

```
{% layout none %}
```

## paginate

将结果集拆分成多页是有必要的。  
`paginate` 和 `for` 结合可以将结果集拆分成多页。  
必须像下面的样子  

```
{% paginate collection.products by 5 %}  
  {% for product in collection.products %}
    <!--show product details here -->
  {% endfor %}
{% endpaginate %}
```
`by`参数后面的数字应该在 1 到 50 之间， 作用是告诉 `paginate` 一页有多少数据。  
使用`paginate`对象时，你可以使用[paginate](paginate.md)的属性。  

## raw

有时候，我们有段文本不想被解析，怎么办呢？  
raw 标签就可以做到这个。  


```
{% raw %}{{ 5 | plus: 6 }}{% endraw %} is equal to 11.
```

```
{{ 5 | plus: 6 }} is equal to 11.
```




