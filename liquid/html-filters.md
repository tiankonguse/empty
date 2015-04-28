# HTML 过滤器


## img_tag

生成一个图片标签。  

```
{{ 'smirking_gnome.gif' | asset_url | img_tag }}
```

输出如下  

```
<img src="//cdn.shopify.com/s/files/1/0147/8382/t/15/assets/smirking_gnome.gif?v=1384022871" alt="" />
```

`img_tag` 接受两个参数用来输出`alt`属性和`class`属性。  
第一个参数用来当做`alt`属性值，剩余的参数输出当做`class`属性值。  

```
{{ 'smirking_gnome.gif' | asset_url | img_tag: 'Smirking Gnome', 'cssclass1 cssclass2' }}
```

输出如下  

```
<img src="//cdn.shopify.com/s/files/1/0147/8382/t/15/assets/smirking_gnome.gif?v=1384022871" alt="Smirking Gnome" class="cssclass1 cssclass2" />
```

`img_tag`标签可以被下面的对象使用  

* [product](product.md)  
* [variant](variant.md)  
* [line item](line\_item.md)  
* [collection](collection.md)  
* [image](image.md)  

```
{{ product | img_tag }}
{{ variant | img_tag: 'alternate text' }}
{{ line_item | img_tag: 'alternate text', 'css-class' }}
{{ image | img_tag: 'alternate text', 'css-class', 'small' }}
{{ collection | img_tag: 'alternate text', 'css-class', 'large' }}
```

输出如下  

```
<img src="//cdn.shopify.com/s/files/1/0159/3350/products/red_shirt_small.jpg?v=1398706734" alt="Red Shirt Small" />
<img src="//cdn.shopify.com/s/files/1/0159/3350/products/red_shirt_small.jpg?v=1398706734" alt="alternate text" />
<img src="//cdn.shopify.com/s/files/1/0159/3350/products/red_shirt_small.jpg?v=1398706734" alt="alternate text" class="css-class" />
<img src="//cdn.shopify.com/s/files/1/0159/3350/products/red_shirt_small.jpg?v=1398706734" alt="alternate text" class="css-class" />
<img src="//cdn.shopify.com/s/files/1/0159/3350/products/shirts_collection_large.jpg?v=1338563745" alt="alternate text" class="css-class" />
```

## script_tag

生成一个脚本标签  

```
{{ 'shop.js' | asset_url | script_tag }}
```

输出如下  

```
<script src="//cdn.shopify.com/s/files/1/0087/0462/t/394/assets/shop.js?28178" type="text/javascript"></script>
```


## stylesheet_tag

生成一个样式标签  

```
{{ 'shop.css' | asset_url | stylesheet_tag }}
```

输出如下  

```
<link href="//cdn.shopify.com/s/files/1/0087/0462/t/394/assets/shop.css?28178" rel="stylesheet" type="text/css" media="all" />
```

