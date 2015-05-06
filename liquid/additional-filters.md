# 附加的过滤器

## date

将时间戳转化为一个时间。  

```
{{ article.published_at | date: "%a, %b %d, %y" }}
```

输出如下  

```
Tue, Apr 22, 14
```

* `%a` 缩写的周几
* `%A` 周几
* `%b`  简写月份
* `%B` 月份
* `%c` 日期与时间(Tue Apr 22 11:16:09 2014)
* `%d` 前缀0的一月第几天
* `%-d` 一月的第几天
* `%D` 日期(dd/mm/yy)
* `%e` 一月的第几天
* `%F` 日期(yyyy-mm-dd)
* `%H` 前缀0的24小时的小时
* `%I` 12小时的小时
* `%j` 前缀0的一年第几天
* `%k` 24小时的小时
* `%m` 前缀0的月
* `%M` 前缀0的分钟
* `%p` 上下午
* `%r` 12小时时间(%I:%M:%S %p)
* `%R` 24小时时间(%H:%M)
* `%T` 24小时的时间(%H:%M:%S)
* `%U` 几年第几周(第一个周日算起) 
* `%W` 几年第几周(第一个周一算起)
* `%w` 数字周几(0代表周日)
* `%x` 日期(mm/dd/yy)
* `%X` 时间(hh:mm:ss)
* `%y` 缩写的两位年份
* `%Y` 完整的年份
* `%Z` 时区名字


## default

忽略。  

## default_errors

忽略这个过滤器  

## default_pagination

创建一个页数集合。  
常常和[paginate](paginate.md)联合使用。  

```
{{ paginate | default_pagination }}
```

输出如下  

```
<span class="page current">1</span>
<span class="page"><a href="/collections/all?page=2" title="">2</a></span>
<span class="page"><a href="/collections/all?page=3" title="">3</a></span>
<span class="deco">&hellip;</span>
<span class="page"><a href="/collections/all?page=17" title="">17</a></span>
<span class="next"><a href="/collections/all?page=2" title="">Next &raquo;</a></span>
```
## highlight

忽略这个命令  

## highlight_active_tag

忽略这个命令。  

## json

将字符串转化为json.  

```
var content = {{ pages.page-handle.content | json }};
```

输出如下  

```
var content = "\u003Cp\u003E\u003Cstrong\u003EYou made it! Congratulations on starting your own e-commerce store!\u003C/strong\u003E\u003C/p\u003E\n\u003Cp\u003EThis is your shop\u0026#8217;s \u003Cstrong\u003Efrontpage\u003C/strong\u003E, and it\u0026#8217;s the first thing your customers will see when they arrive. You\u0026#8217;ll be able to organize and style this page however you like.\u003C/p\u003E\n\u003Cp\u003E\u003Cstrong\u003ETo get started adding products to your shop, head over to the \u003Ca href=\"/admin\"\u003EAdmin Area\u003C/a\u003E.\u003C/strong\u003E\u003C/p\u003E\n\u003Cp\u003EEnjoy the software,  \u003Cbr /\u003E\nYour Shopify Team.\u003C/p\u003E";
```
## weight_with_unit

格式化变量的重量。重量的单位在[General Settings](general.md)设置。  

```
{{ product.variants.first.weight | weight_with_unit }}
```

输出如下  

```
24.0 kg
```

总量的单位可以通过参数来自定义。  


```
{{ variant.weight | weight_with_unit: variant.weight_unit }}
```

输出如下  

```
52.9 lb
```
