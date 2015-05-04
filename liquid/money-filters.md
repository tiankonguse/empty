# Money 过滤器

这个一般用不上，可以忽略下面的教程。  


## money

基于HTML上的货币格式规范化金钱。  

```
{{ 145 | money }}
```

输出如下  

```
<!-- if "HTML without currency" is ${{ amount }} -->
$1.45
<!-- if "HTML without currency" is €{{ amount_no_decimals }} -->
€1
```


## money_with_currency

使用HTML上的货币格式规范化货币价格。  

```
money_with_currency
```

输出如下  

```
<!-- if "HTML with currency" is ${{ amount }} CAD -->
$1.45 CAD
```


## money_without_trailing_zeros

使用HTML上的货币格式规范价格:变成小数，并删除后缀0.  

```
<!-- if "HTML with currency" is ${{ amount }} CAD -->
{{ 2000 | money_without_trailing_zeros }}
```

输出如下  


```
$20
```

只有小数的后缀0会删除，其他数字不会被删除。  

```
<!-- if "HTML with currency" is ${{ amount }} CAD -->
{{ 145 | money_without_trailing_zeros }}
```

输出如下  


```
$1.45
```

## money_without_currency

使用小数规范价格。  

```
{{ 145 | money_without_currency }}
```

输出如下  

```
1.45
```

