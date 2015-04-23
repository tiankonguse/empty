# handle

## handle 是什么 

handle 用于访问 Liquid 对象的属性。  
一般情况下，把对象的标题中的空白和特殊字符使用连接符替换后的就可以得到 handle。  
Liquid 里面的每一个对象(product, collection, blog, link list) 都有一个 handle.  

例如一个带有"About Us"标题的页面，在Liquid里可以通过他的handle `about-us`访问。  

例如下面的例子。  

```
<!-- the content of the About Us page -->
{{ pages.about-us.content }}
```
## handles 怎么创建的  

一个以"Shirt"为标题的 product 会自动的被赋予名字为 `shirt` 的handle。  
如果已经存在handle `Shirt` 的话，handle 将会自增赋值。  
换句话说，所有的handle是`Shirt`的products ，在第一个之后，将会被赋予`shirt-1`,`shirt-2`等等.  

在handle中，标题中的空白会被替换成连接符`-`.  
例如标题"My Shiny New Title"将会得到名为`my-shiny-new-title`的handle.  


handle 同时也决定了对象的URL.  
例如一个以`about`为handle的页面，将会得到 [http://github.tiankonguse.com/about][about]  

一个系统往往依赖于页面，产品和链接的静态handle.  
为了防止系统产生死链，当你修改对象的标题时，往往不会自动更新对象的handle.  

## 通过handle访问对象的属性

很多时候，你可能知道你想使用对象的handle和对应的属性名。  
这个时候，你可以通过方括号`[]`或点`.`，来访问对象的属性。  

```
{{ pages.about-us.title }} 
{{ pages["about-us"].title }}
```

将会输出

```
About Us
About Us
```

注意，在上面的例子中，我们使用的是`pages`而不是`page`.  

你也可以使用这个方法访问定制主题中的对象。  
这样设计是为了使用这些模板主题的人能够选择那些内容可以再模板中展示。  

```
{% for product in collections[settings.home_featured_collection].products %}
    {{ product.title }}
{% endfor %}
```

将会得到下面的内容  

```
Awesome Shoes
Cool T-Shirt
Wicked Socks
```


[about]: http://github.tiankonguse.com/about.html
