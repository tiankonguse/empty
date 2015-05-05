# 字符串过滤器

字符串过滤器主要用在输出或者字符串[]类](types.md)型的变量上。  

## append

在字符串后面追加内容。  

```
{{ 'sales' | append: '.jpg' }}
```

输出如下  

```
sales.jpg
```


## camelcase

转换字符串为骆驼拼写法。  

```
{{ 'coming-soon' | camelcase }}
```

输出如下  

```
ComingSoon
```


## capitalize

将字符串的第一个单词变为大写。  

```
{{ 'capitalize me' | capitalize }}
```

输出如下  

```
Capitalize me
```

## downcase

字符串转换为小写  

```
{{ 'UPPERCASE' | downcase }}
```

输出如下  

```
uppercase
```

## escape

对HTML标签进行转义，原样输出。  

```
{{ "<p>test</p>" | escape }}
```

输出如下  

```
<!-- The <p> tags are not rendered -->
<p>test</p>
```

## handle/handleize

格式化字符串为 [handle](handle.md)

```
{{ '100% M & Ms!!!' | handleize }}
```

输出如下  

```
100-m-ms
```

## md5

转换字符串到md5.  
下面的例子是根据用户的邮箱映射到头像名。  

```
<img src="https://www.gravatar.com/avatar/{{ comment.email | remove: ' ' | strip_newlines | downcase | md5 }}" />
```

输出如下  

```
<img src="https://www.gravatar.com/avatar/2a95ab7c950db9693c2ceb767784c201" />
```

## newline_to_br

在字符串中的换行符中加入HTML的换行符标签`<br >`  

```
{% capture var %}
One
Two
Three
{% endcapture %}
{{ var | newline_to_br }}
```

输出如下  

```
One <br>
Two<br>
Three<br>
```

## pluralize

根据指定的值来判断输出单数还是负数。  
第一个参数是单数字符串，第二个参数是负数字符串。  

```
{{ cart.item_count }}
{{ cart.item_count | pluralize: 'item', 'items' }}
```

输出如下  

```
3 items
```

## prepend

在字符串前边增加一段内容。  

```
{{ 'sale' | prepend: 'Made a great ' }}
```

输出如下  

```
Made a great sale
```

## remove

删除所有匹配的子串  

```
{{ "Hello, world. Goodbye, world." | remove: "world" }}
```

输出如下  

```
Hello, . Goodbye, .
```

## remove_first

删除第一次出现的子串  

```
{{ "Hello, world. Goodbye, world." | remove_first: "world" }}
```

输出如下  

```
Hello, . Goodbye, world.
```


## replace

替换匹配的所有的子串。  

```
<!-- product.title = "Awesome Shoes" -->
{{ product.title | replace: 'Awesome', 'Mega' }}
```

输出如下  

```
Mega Shoes
```

## replace_first

替换第一次出现的字符串。  

```
<!-- product.title = "Awesome Awesome Shoes" -->
{{ product.title | replace_first: 'Awesome', 'Mega' }}
```

输出如下  

```
Mega Awesome Shoes
```

## slice

`slice`主要根据指定的参数，返回一个子串。  
第一个参数表示子串的起始位置，第二个参数用于标识子串的长度。  
若第二个参数未指定，返回的子串长度为1.  

```
{{ "hello" | slice: 0 }}
{{ "hello" | slice: 1 }}
{{ "hello" | slice: 1, 3 }}
```

输出如下  

```
h
e
ell
```

如果传递的第一个参数是负值，则他从子串结尾倒数第几个开始。  

```
{{ "hello" | slice: -3, 2  }}
```

输出如下  

```
el
```

## split

`split`接受一个子串当做参数。  
子串作为分隔符将字符串分割为一个数组。  

```
{% assign words = "Uses cheat codes, calls the game boring." | split: ' ' %}
First word: {{ words.first }}
First word: {{ words[0] }}
Second word: {{ words[1] }}
Last word: {{ words.last }}
All words: {{ words | join: ', ' }}

{% for word in words %}
{{ word }}
{% endfor %}
```

输出如下  

```
First word: Uses
First word: Uses
Second word: cheat
Last word: boring.
All words: Uses, cheat, codes,, calls, the, game, boring.

Uses cheat codes, calls the game boring.
```

## strip

删除字符串的两边的空白（前缀空白和后缀空白）。  

```
{{ '   too many spaces      ' | strip }}
```

输出如下  

```
too many spaces
```

## lstrip

删除字符串的左边的空白（前缀空白）。  

```
"{{ '   too many spaces           ' | lstrip }}"
```

输出如下  

```
<!-- Notice the empty spaces to the right of the string -->
too many spaces
```

## rstrip

删除字符串的右边的空白（后缀空白）。  

```
{{ '              too many spaces      ' | rstrip }}
```

输出如下  

```
                 too many spaces
```

## strip_html

删除字符串中的html的标签。  

```
{{ "<h1>Hello</h1> World" | strip_html }}
```

输出如下  

```
Hello World
```

## strip_newlines

从字符串中删除换行符。  

```
{{ product.description | strip_newlines }}
```

## truncate

根据指定的参数`x`, 将字符串缩写为`x`个字符。  
在缩写字符串后面会跟一个省略号。  

```
{{ "The cat came back the very next day" | truncate: 10 }}
```

输出如下  

```
The cat...
```

## truncatewords

根据指定的参数`x`, 将字符串缩写为`x`个单词。  
在缩写字符串后面会跟一个省略号。  

```
{{ "The cat came back the very next day" | truncatewords: 4 }}
```

输出如下  

```
The cat came back...
```

## uniq

删除数组中重复元素。  

```
{% assign fruits = "orange apple banana apple orange" %}
{{ fruits | split: ' ' | uniq | join: ' ' }}
```

输出如下  

```
orange apple banana
```

## upcase

将字符串转换为大写。  

```
{{ 'i want this to be uppercase' | upcase }}
```

输出如下  

```
I WANT THIS TO BE UPPERCASE
```

## url_escape

将字符串中在URL中是特殊字符的全部进行转义，一般用于对url进行转义。  

```
{{ "<hello> & <shopify>" | url_escape }}
```

输出如下  

```
%3Chello%3E%20&%20%3Cshopify%3E
```

## url_param_escape

将字符串中在URL中是特殊字符的全部进行转义，包括字符`&`， 一般用于当做URL的value值，对value进行转义。  

```
{{ "<hello> & <shopify>" | url_param_escape }}
```

输出如下  

```
%3Chello%3E%20%26%20%3Cshopify%3E
```


