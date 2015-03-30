# vim学习笔记之开始编辑

## 学习vim之简单编辑。

### 开始编辑

<b>官方文档</b>

```text
i     Insert text before the cursor .
	
```

<b>我的理解</b>
```text
->esc  ->i
```

<b>小提示</b>
```text
输入i后，就可以输入内容了
```


### 保存文档

<b>官方文档</b>

```text
:w[rite] [++opt]      Write the whole buffer to the current file.  This is
                      the normal way to save changes to a file.  It fails
                      when the 'readonly' option is set or when there is
                      another reason why the file can't be written.
                      For ++opt see ++opt, but only ++bin, ++nobin, ++ff
                      and ++enc are effective.

:w[rite]! [++opt]     Like ":write", but forcefully write when 'readonly' is
                      set or there is another reason why writing was
                      refused.
                      Note: This may change the permission and ownership of
                      the file and break (symbolic) links.  Add the 'W' flag
                      to 'cpoptions' to avoid this.
```
<b>我的理解</b>

```text
保存文档 ->esc ->w/
如果文档未命名的话: ->esc ->w name / 
```

<b>小提示</b>
```text
文档不太适合初学者看。
```


## 学习vim之删除光标所在字符。

### 删除字符

<b>官方文档</b>

```text

["x]x                   Delete [count] characters under and after the cursor
                        [into register x] (not linewise).  Does the same as
                        "dl".
                        The <Del> key does not take a [count].  Instead, it
                        deletes the last character of the count.
                        See :fixdel if the <Del> key does not do what you
                        want.  See 'whichwrap' for deleting a line break
                        (join lines).  {Vi does not support <Del>}
```
<b>我的理解</b>

```text
删除字符: ->esc ->x
```

<b>小提示</b>
```text
文档中说可以删除多个字符。
```


##links
   * [目录](readme.md)


