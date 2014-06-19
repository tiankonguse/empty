<h1>优化网站的加载速度</h1>


<h2>使http的请求数量最小</h2>

这里有几个方法减少请求页面的方法。
<ul>
<li>Combined files : 把所有的　scripts 文件放在一个文件里</li>
<li>css sprites : 减少　css 脚本里对图片的请求。使用一种图片，然后使用　background-position 来显示对应的片段。</li>
<li>Inline images : 使用　data : URL scheme 来内嵌图片。</li>
<li></li>
<li></li>
</ul>

<h2>使用内容分布式网络储存(CDN)</h2>


<h2>给　head 增加一个　Expires 或　Cache-Control </h2>

<h2>Gzip 压缩</h2>

<h2>把样式表放在最上面</h2>

<h2>把 Scripts 放在最下面</h2>

<h2>避免 CSS 期限</h2>

background-color: expression( (new Date()).getHours()%2 ? "#B8D4FF" : "#F08A00"  );

<h2>把　javascript 和　css 放在外部文件</h2>


<h2>减少　DNS 的查找时间</h2>


<h2>最小化 javascript和css</h2>

<h2>避免重定向</h2>

<h2>删除重复的脚本</h2>

php可以使用insertScript　来避免重复引入同一个脚本。

<h2>配置　Etags</h2>

<h2>让　ajac 可缓存</h2>

<h2>及时的 flush 缓存</h2>

    ... <!-- css, js -->
    </head>
    <?php flush(); ?>
    <body>
      ... <!-- content -->

<h2>ajax 使用 get 请求</h2>

