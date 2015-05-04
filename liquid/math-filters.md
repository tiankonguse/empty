# 数学函数过滤器

数学函数过滤器可以使用简单的数学运算。  

数学过滤器可以和其他过滤器一起使用，规则是从左到右。  
例如下面的例子先减去一个数，再乘以一个数，最后除以一个数。  

```
You save {{ product.compare_at_price | minus: product.price | times: 100.0 | divided_by: product.compare_at_price }}%
```


## ceil


向上取整  

```
{{ 4.6 | ceil }} 
{{ 4.3 | ceil }} 
```

输出如下  

```
5
5
```


## divided_by


除以一个数  

```
<!-- product.price = 200 -->
{{ product.price | divided_by: 10 }}
```

输出如下  

```
20
```


## floor

向下取整  


```
{{ 4.6 | floor }}
{{ 4.3 | floor }}
```

输出如下  

```
4
4
```

## minus

减去一个数  

```
<!-- product.price = 200 -->
{{ product.price | minus: 15 }}
```

输出如下  


```
185
```

## plus

加上一个数  

```
<!-- product.price = 200 -->
{{ product.price | plus: 15 }}
```

输出如下  

```
215
```

## round

四舍五入，默认是整数。  
也可以指定保留小数的位数  

```
{{ 4.6 | round }}
{{ 4.3 | round }}
{{ 4.5612 | round: 2 }}
```

输出如下  

```
5
4
4.56
```


## times

乘以一个数。  


```
<!-- product.price = 200 -->
{{ product.price | times: 1.15 }}
```

输出如下  

```
230
```


## modulo

求余数  

```
{{ 12 | modulo:5 }}
```

输出如下  

```
2
```
