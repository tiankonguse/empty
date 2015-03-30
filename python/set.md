# python 集合set

set（集合）：无序不重复的元素集  

```
basket = ['apple','orange','apple','pear','apple','banana']

fruit=set(basket)
# set(['orange', 'pear', 'apple', 'banana'])

'orange' in fruit 
# True

a=set('abracadabew') 
#set(['a', 'c', 'b', 'e', 'd', 'r', 'w'])

b=set('wajgwaoihwb')
# set(['a', 'b', 'g', 'i', 'h', 'j', 'o', 'w'])

a-b    #差
# set(['c', 'r', 'e', 'd'])

a|b   #并
# set(['a', 'c', 'b', 'e', 'd', 'g', 'i', 'h', 'j', 'o', 'r', 'w'])  

a&b   #交
# set(['a', 'b', 'w'])  

a^b   #(并-交)
set(['c', 'e', 'd', 'g', 'i', 'h', 'j', 'o', 'r'])
```



