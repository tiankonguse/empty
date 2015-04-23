# 简介

Liquid是一个被Shopify创造的，开源的，基于Ruby的模板语言．  
它是Shopify 主题的核心，而且它有动态加载内容功能．

Liquid 使用 标签，对象和过滤器来动态加载内容。  
一大堆这些动态内容组成的Liquid模板文件构成了一个主题。  
关于主题的更多知识，请参考[主题制作][templates]

## 标签 

标签是告诉模板做什么的编程逻辑语法。  

```
{% if user.name == 'elvis' %}
  Hey Elvis
{% endif %}
```

更多参考[标签介绍][tags]  

## 对象 

对象包含一些属性，可以动态的展示在页面上。

```
<!-- product = {title : "tiankonguse's record" }  -->
{{ product.title }}
<!-- Output: tiankonguse's record  -->
```

更多参考[对象介绍][objects]

## 过滤器 

过滤器用于修改输出的字符串，数字，变量和对象。  

```
{{ 'sales' | append: '.jpg' }} 
<!-- Output: sales.jpg -->
```

更多参考[过滤器介绍][filters]


[filters]: filters.md
[objects]: objects.md
[tags]: tags.md
[templates]: templates.md
