# 轻松学会 HTML 技术 

## 前言

HTML 很容易使用， 它就是因为这样才被设计出来的。  
不是成为程序员后才能使用他，任何人都可以使用它。  
如果你能编辑文本文件，你就能写HTML（如果你会写邮件，你就肯定会编辑文本文件）。  
如果之前你曾经尝试学习HTML，但是失败了，那肯定是有人误导你了。  


这个教程会快速简洁的讲解HTML的组成，还会通过一些实际例子让你能够快速制作自己的页面(比如今天下午)。  
这个教程打印下来大概有14页纸张，但是你只需要先看一个小时，然后停下来运行你的页面。  


在这里，你将会创建很多小的页面，而且可以浏览他们。  
这些真的不需要任何经验，只不过你需要不断的练习，然后熟悉适应这些新概念。  
如果你的浏览器支持 frames, 打开这个 [HTML 测试基地][html-f-testbed]， 然后你可以在一个 frame 里输入 HTML 代码， 在另一个地方看到结果。  
为了友好的展示，请设置输入和输出的frame大小。  


如果你的浏览器不支持 frames 或者你想制作真实的页面， 你就需要一个真实的文本编辑器了。  
在 Mac 上可以使用 TeachText； 在 Unix 上可以使用 pico； 在windows 上可以使用 Notepad 。当然你也可以使用你想使用的编辑器。  
（译者注：对于tiankonguse，没用过Mac； 在Unix下使用vim和gedit；在windows下使用 Notepad++ 和 sublime）  
你应该把你的HTML文件保存为 `.html` 或 `.htm` 后缀。  
然后你就可以使用浏览器访问你创建的HTML文件，当文件有修改时，可以使用 `F5` 刷新重新加载。  

## HTML 基础

### HTML是什么

尽管 HTML 的含义是 ** HyperText Markup Language ** ， 但是它不像 Java, Perl, C 或者 BASIC 那样的真实编程语言， 它非常简单。  
它与报社编辑的标记符号的概念类似，用于描述文本和图片集合如何展示给浏览者。  

### 介绍网页

一个网页包含一个 HTML 文件和附加的若干图片等资源。  
一个 HTML 文件(一个普通的文件)包含了所有的需要展示的文本，就像万能胶一样把文本和图片粘在合适的位置，显示合适的样式。  

编写一个HTML就是组织你想展示的文本，然后在你想展示的位置插入标签(tags)。  
标签以 `<` 字符开始， 以 `>` 字符结束，可以使浏览器展示特殊的效果，比如斜体，黑体，字体大小，或者显示图片，或者超链接指向新的页面。  
尽管 HTML 提供了很多标签，我们不需要全部记住他们，我们只需要能够快速查到他们就行了。  

学习HTML时令人高兴的一件事是你可以通过查看源码了解到其他人怎么实现网页的。  
看大量的源代码。查看任何让你感兴趣如何实现的页面的源代码。  
任何会使用HTML的人都是通过查看其他人的HTML代码学习的，互联网很大，有很多值得学习的东西。  


### 介绍 HTML 标签

标签有一个简单的结构。  
他们以 `<` 开始， 以 `>` 结束。  
在 `<>` 中间的是标签名字，当然也可能有一些与标签相关联的属性。  
大部分属性也会有一个属性值。  
一些属性是必须的，另一些是可选的。  
标签一般的形式是 `<tagname attribute1="value1" attribute2="value2" ... >`。  
标签名称和标签属性名是大小写不敏感的，但是属性值是大小写敏感的。  
标签名必须是在第一个位置，其他属性则没有位置限制。  
所以你可以这样写标签 `<TAGNAME ATTRIBUTE2="value2" ATTRIBUTE1="value1" ... >`。  

不同的人有不同的书写方式， 按你自己习惯的风格书写吧。  
不同的标签一般做不同的事。  
比如，使用 `<img>` 标签用于在网页中显示图片。  

```
<img src="blueribbon.gif">
```
将会显示下面的图片

<img src="http://www.jmarshall.com/easy/html/blueribbon.gif">

这行代码的含义是在这个地方显示 `blueribbon.gif` 图片。  
注意 `src` 属性指定图片的 URL, 可以是相对位置，也可以是绝对位置。  
上面的例子使用绝对URL将会是下面的样子。  

```
<img src="http://www.jmarshall.com/easy/html/blueribbon.gif">
```

### 容器标签

像`<img>`这些标签，仅仅代表自己，不会影响周围的其他东西。  
还有一些标签有一个开始标签和一个结束标签，将会影响中间的所有内容。  
一般称他们为容器标签，这是因为他们在开始和结束位置之间有其他东西。  
例如，使文本变成粗体，你只需要在需要变粗的地方开始标记，然后需要正常显示的位置结束标记。  
使用 `<b>` 和 `</b>` 做到粗体显示， 比如  

```
This is normal text.  <b>This is bold text.</b>  Normal again.
```

将会显示如下  

This is normal text.  <b>This is bold text.</b>  Normal again.  

不管容器标签名是什么，所有的容器标签都以 `</tagname>` 结束。  
例如在这个例子中， `<b>` 标签以 `</b>` 结束。  
结束标签不像开始标签那样有属性，结束标签没有。  

### 很酷的地方

一个使所有页面互相连接起来组成了网站的标签是 `<a>`。  
`<a>` 标签是一个连接新页面的标签，而且很容易使用。  
比如下面的例子，展示和怎么链接指向 电子前沿基金会的 Blue Ribbon 页面。  

```
Read about <a href="http://www.eff.org/blueribbon.html">issues that affect you</a>.
```

这将会显示为 Read about <a href="http://www.eff.org/blueribbon.html">issues that affect you</a>.  

注意这里有一个开始标签 `<a href="http://www.eff.org/blueribbon.html">` 和一个结束标签 `</a>`, 而且任何在这之间的内容`issues that affect you` 被渲染为用户可以点击的显眼的蓝色有下划线的超链接。  

注意， 属性 `href` 的值 `http://www.eff.org/blueribbon.html` 就是当用户点击链接的时候需要跳转的URL（网页地址）。  

### 链接的更多介绍

#### 图片链接

你可以在 `<a>` 和 `</a>` 标签之前插入图片链接 `<img>` 。  
这样用户就可以点击图片跳转到链接页面。  

#### 邮箱链接

对于邮箱链接，把 `href` 设置成 `mailto:email-address`。  
例如  

```
Tell <a href="mailto:president@whitehouse.gov">the President</a> what you think.
```

将会渲染为 Tell <a href="mailto:president@whitehouse.gov">the President</a> what you think.  

### 页面内的链接

为了链接向同一个页面的其他地方，第一步需要在你想跳转到的位置创建一个名字锚  
例如 `<a name="anchorname"></a>`  
注意，和使用 `<a>` 标签不同， 事实上 `<a>`最初的目的就是为了锚。  
由于锚只是为了标记页面的一个位置，所以不需要在标签之间填充东西。  

一旦锚在目标页面存在，使用`<a href>`链接想目标页面, 然后在目标链接后面附加上 `#anchorname`。  
例如  

```
Read about <a href="http://www.jmarshall.com/easy/html/#lists">HTML lists</a>.
```

当想链接想同一个页面的其他位置时， 可以省略其余的UR. 例如  

```
<a href="#toc">Back to Table of Contents</a>
```

### 了解HTML文件

现在你理解了标签和容器标签是是什么。  
这里教你怎么使用正确的方法制作 HTML文件：确保你的HTML文件在容器标签`<html>`中是封闭的。换句话说就是确保`<html>`标签是文件开始标签， `</html>`是文件的结束标签。  

理论上，`<html>`标签纸能包含两个东西:`<head>`标签和 `<body>`标签。  
在`<body>`标签内部，你可以把你所有的页面放在里面。  
比如显示的文本、图片、超链接等等都要放在`<body>`标签里  

可选的`<head>`部分放在`<body>`前面，主要包含一些文档的描述信息。  
当`<head>`存在的时候，可以只包含用于在浏览器顶部显示的`<title>`。  

这里有一个简单的以 `hello, world`为标题的HTML文件。  

```
<html>

<head>
<title>Hello, world</title>
</head>

<body>
Hello, world.
</body>

</html>
```

如果你不想要标题的话， 可以把标题那一行删除了。  
如果这让你感到困惑，不要担心。  
只需要严格准守`<html><body>`在文件的开头，`</body></html>`在文件的结尾就行了，这样就会神奇般的生成一个合法的HTML文件了。  

### 断行和空白  

你可以劲量多的添加空格和空行(统称空白)来使你的HTML文件易于阅读。  
不管连续有多少个空白，浏览器都会将它们显示为一个空格。  

这个教程使用一个缩进作为样例，但是你应该使用易于阅读的缩进。  

使用`<p>`标签可以开始一个新的段落。  
浏览器会依靠浏览窗口的大小，合适的显示所有的文本(自动换行)。  
如果你想强制开始新的一行，可以使用 `<br>`比我爱你。  

现在你学的显示图片和超链接已经可以写一些网页了。  
尝试一下吧， 你会发现那些都按你想的展示出来了。  
可以制作一个简单的页面，然后在浏览器中欣赏一下。  

### 少量有用的标签

* `<i></i>` 斜体
* `<tt></tt>` 打印字体
* `<h1></h1> ~ <h6></h6>` 展示不同样式的头标题
* `<hr>` 水平线
* `<center> </center>` 居中
* `<blockquote> </blockquote>` 缩进被填充的文字
* `<pre> </pre>` 源代码

## HTML 入阶

### 列表

HTML 提供了一些简单的方法来显示数字列表和无序列表。  

分别使用　`<ol>` 和　`<ul>` 容器标签来生成有序或者无序列表。  

在容器标签中，使用`<li>`标签来表示列表的一项内容。  

例如下面的HTML代码  


```
This is an ordered list:
<ol>
<li>First item
<li>Second item
<li>Third item
</ol>

This is an unordered list:
<ul>
<li>First item
<li>Second item
<li>Third item
</ul>
```

将会显示如下  

This is an ordered list:
<ol>
<li>First item
<li>Second item
<li>Third item
</ol>

This is an unordered list:
<ul>
<li>First item
<li>Second item
<li>Third item
</ul>

请确保使用闭合标签`</ol>`,`</ul>`和`</dl>`，否则页面剩下将会都是列表中最后一项。  

### 注释

你可以把注释内容放到HTML页面中，这些注释不会显示出来的。  
这些注释主要为了向那些看你HTML源代码的人解释你为什么样这样写你的代码。  
那个看代码的人可能是别人，但是在未来，更有可能是你。  

使用　`<!--` 开始注释，使用`-->`结束注释。  

例如  

```
<!-- This is a comment, and won't display to the user -->
<!-- comment examples inserted by JSM on 9-23-96, for clarity -->
```

不要把私有信息放到注释里，因为任何看源代码的人都能看到那些。  
特别注意，不要把　HTML标签放到注释里，因为大多数浏览器会把　`>` 符号当做结束标签。  

### 表格


就像上面的更多标签一样，HTML的表格标签可以让你把数据单元以数组的形式展现。  
使用这个可以让文本右对齐或者像购物商店的页卡一样一列一列的排列在那里。  
只要你明白你想在每个单元格里显示什么，表格将会很容易使用的。  
HTML的表格定义规范虽然有些改变，但是现在它已经十分稳定了。  
接下来将会告诉你怎么制作所有浏览器都兼容的表格。  

* 表格需要使用标签`<table>`  
* 在表格`<table>`的每一行里需要使用标签`<tr>`  
* 在行标签`<tr>`里面，所有的单元格需要使用标签`<td>`  
* 每一个单元格可以包含你想展示的任何东西-链接，图片，列表或者其他表格。  


行标签从上到下展示，单元格心欧诺个左到右展示。  
如果你想让单元格里的内容比较突出，可以使用表格`<table>`的`border`属性。  

样例如下  


```
<table border>
<tr>
    <td>northwest</td>
    <td>northeast</td>
</tr>
<tr>
    <td>southwest</td>
    <td>southeast</td>
</tr>
</table>
```


将会显示为  

<table border>
<tr>
    <td>northwest</td>
    <td>northeast</td>
</tr>
<tr>
    <td>southwest</td>
    <td>southeast</td>
</tr>
</table>


大多说浏览器不需要`</td>`和`</tr>`标签。  
因为他们假设遇到下一个单元格和行标签的开始符号时，可以认为上一个标签结束了。  

所以你可能会遇到没有带结束标签的表格。  

译者注：不过这里建议所有的标签都加上结束标签。  

### 跨越多行或多列的单元格

有时候，你可能想要让一个单元格占用多行或者多列。  
这个时候，你就可以使用`<td>`标签的`colspan`或者`rowspan`属性,然后只需要不去定义单元格可能会占用的单元格即可。  

例如  

```
<table border>
<tr>
    <td rowspan=2>west</td>
    <td>northeast</td>
</tr>
<tr>
    <!-- Don't define "southwest", since it's overlaid by "west" -->
    <td>southeast</td>
</tr>
</table>
```

将会显示如下  

<table border>
<tr>
    <td rowspan=2>west</td>
    <td>northeast</td>
</tr>
<tr>
    <!-- Don't define "southwest", since it's overlaid by "west" -->
    <td>southeast</td>
</tr>
</table>


### 在单元格内内容对齐

通常，所有的内容会左对齐和垂直居中对齐。  
在`<td>`标签内使用`aligh`和`valign`可以实现水平对齐和垂直对齐。  

* `aligh` 的值可以是`left`，`right`，`center`。  
* `valign`的值可以是`top`，`middle`，`bottom`，`baseline`。  


比如这个，无边框的杂货店收据的价格就是右对齐的。  

```
<table>
<tr>
    <td>laundry detergent</td>
    <td align=right>$4.99</td>
</tr>
<tr>
    <td>cat food</td>
    <td align=right>$128.00</td>
</tr>
</table>
```

显示如下  

<table>
<tr>
    <td>laundry detergent</td>
    <td align=right>$4.99</td>
</tr>
<tr>
    <td>cat food</td>
    <td align=right>$128.00</td>
</tr>
</table>

当然，你也可以把`aligh`和`valign`属性加到`<tr>`上来影响一行的所有的单元格。  

### 表单



## HTML 技巧

## HTML 资料


翻译来源: [HTML Made Really Easy][jmarshall-easy-html] 

[jmarshall-easy-html-testbed]: http://jmarshall.com/easy/html/testbed.html
[jmarshall-easy-html-f-testbed]: http://jmarshall.com/easy/html/f_testbed.html
[jmarshall-easy-html]: http://jmarshall.com/easy/html/
