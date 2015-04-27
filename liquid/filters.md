# Filters

过滤器是一个修改数字，字符串，变量和对象输出的简单的方法．  
他们放在输出标签`{{ }}`内,并且使用管道符号`|`分隔．  

```
<!-- product.title = "Awesome Shoes" -->
{{ product.title | upcase }}
```

输出如下  

```
AWESOME SHOES
```

上面的例子中，`product`是一个对象，`title`是这个对象的属性，`upcase`是使用的一个过滤器．  


有些过滤器需要传递一个参数的．  



```
{{ product.title | remove: "Awesome" }}
```

输出如下  


```
Shoes
```

多个过滤器可以应用与同一个输出．  
他们从左到右一次应用．  


```
<!-- product.title = "Awesome Shoes" -->
{{ product.title | upcase | remove: "AWESOME"  }}
```

输出如下  

```
SHOES
```


