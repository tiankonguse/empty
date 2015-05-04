# 字符串过滤器



## append


```
{{ 'sales' | append: '.jpg' }}
```

```
sales.jpg
```


## camelcase

```
{{ 'coming-soon' | camelcase }}
```


```
ComingSoon
```


## capitalize

```
{{ 'capitalize me' | capitalize }}
```


```
Capitalize me
```

## downcase

```
{{ 'UPPERCASE' | downcase }}
```


```
uppercase
```

## escape

```
{{ "<p>test</p>" | escape }}
```


```
<!-- The <p> tags are not rendered -->
<p>test</p>
```

## handle/handleize

```
{{ '100% M & Ms!!!' | handleize }}
```


```
100-m-ms
```

## md5

```
<img src="https://www.gravatar.com/avatar/{{ comment.email | remove: ' ' | strip_newlines | downcase | md5 }}" />
```


```
<img src="https://www.gravatar.com/avatar/2a95ab7c950db9693c2ceb767784c201" />
```

## newline_to_br

```
{% capture var %}
One
Two
Three
{% endcapture %}
{{ var | newline_to_br }}
```


```
One <br>
Two<br>
Three<br>
```

## pluralize

```
{{ cart.item_count }}
{{ cart.item_count | pluralize: 'item', 'items' }}
```


```
3 items
```

## prepend

```
{{ 'sale' | prepend: 'Made a great ' }}
```


```
Made a great sale
```

## remove

```
{{ "Hello, world. Goodbye, world." | remove: "world" }}
```


```
Hello, . Goodbye, .
```

## remove_first

```
{{ "Hello, world. Goodbye, world." | remove_first: "world" }}
```


```
Hello, . Goodbye, world.
```


## replace

```
<!-- product.title = "Awesome Shoes" -->
{{ product.title | replace: 'Awesome', 'Mega' }}
```

```
Mega Shoes
```

## replace_first

```
<!-- product.title = "Awesome Awesome Shoes" -->
{{ product.title | replace_first: 'Awesome', 'Mega' }}
```

```
Mega Awesome Shoes
```

## slice

```
{{ "hello" | slice: 0 }}
{{ "hello" | slice: 1 }}
{{ "hello" | slice: 1, 3 }}
```

```
h
e
ell
```


```
{{ "hello" | slice: -3, 2  }}
```

```
el
```

## split

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

```
First word: Uses
First word: Uses
Second word: cheat
Last word: boring.
All words: Uses, cheat, codes,, calls, the, game, boring.

Uses cheat codes, calls the game boring.
```

## strip

```
{{ '   too many spaces      ' | strip }}
```

```
too many spaces
```

## lstrip

```
"{{ '   too many spaces           ' | lstrip }}"
```

```
<!-- Notice the empty spaces to the right of the string -->
too many spaces
```

## rstrip

```
{{ '              too many spaces      ' | rstrip }}
```

```
                 too many spaces
```

## strip_html

```
{{ "<h1>Hello</h1> World" | strip_html }}
```

```
Hello World
```

## strip_newlines

```
{{ product.description | strip_newlines }}
```

## truncate

```
{{ "The cat came back the very next day" | truncate: 10 }}
```


```
The cat...
```

## truncatewords

```
{{ "The cat came back the very next day" | truncatewords: 4 }}
```


```
The cat came back...
```

## uniq

```
{% assign fruits = "orange apple banana apple orange" %}
{{ fruits | split: ' ' | uniq | join: ' ' }}
```


```
orange apple banana
```

## upcase

```
{{ 'i want this to be uppercase' | upcase }}
```


```
I WANT THIS TO BE UPPERCASE
```

## url_escape

```
{{ "<hello> & <shopify>" | url_escape }}
```

```
%3Chello%3E%20&%20%3Cshopify%3E
```

## url_param_escape



```
{{ "<hello> & <shopify>" | url_param_escape }}
```

输出如下  

```
%3Chello%3E%20%26%20%3Cshopify%3E
```


