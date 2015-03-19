# sphinx 简洁

## sphinx 是什么  

Sphinx 是由俄罗斯人Andrew Aksyonoff开发的一个全文检索引擎。  

意图为其他应用提供高速、低空间占用、高结果 相关度的全文搜索功能。  

Sphinx可以非常容易的与SQL数据库和脚本语言集成。  

## sphinx 特性

* 高速的建立索引
* 高性能的搜索
* 可处理海量数据
* 提供了优秀的相关度算法，基于短语相似度和统计（BM25）的复合Ranking方法
* 支持分布式搜索
* 支持短语搜索
* 提供文档摘要生成
* 可作为MySQL的存储引擎提供搜索服务
* 支持布尔、短语、词语相似度等多种检索模式
* 文档支持多个全文检索字段(最大不超过32个)
* 文档支持多个额外的属性信息(例如：分组信息，时间戳等)
* 支持断词


## sphinx 中文分词

中文的全文检索和英文等latin系列不一样，后者是根据空格等特殊字符来断词，而中文是根据语义来分词。  
目前大多数数据库尚未支持中文全文检索.  

国内出现了一些Mysql的中文全文检索的插件，做的比较好的有hightman的中文分词。  
Sphinx如果需要对中文进行全文检索，也得需要一些插件来补充，如 coreseek 和 sfc 。

Coreseek是现在用的最多的sphinx中文全文检索，它提供了为Sphinx设计的中文分词包LibMMSeg  

采用Chih-Hao Tsai MMSEG算法的中文分词器  

sfc（sphinx-for-chinese）是由网友happy提供的另外一个中文分词插件。  
其中文词典采用的是xdict。  


## sphinx mysql应用

Sphinx在mysql上的应用有两种方式：  

- ①、采用API调用，如使用PHP、java等的API函数或方法查询。
  优点是可不必对mysql重新编译，服务端进程“低耦合”，且程序可灵活、方便的调用；
  缺点是如已有搜索程序的条件下，需修改部分程序。推荐程序员使用。
- ②、使用插件方式（sphinxSE）把sphinx编译成一个mysql插件并使用特定的sql语句进行检索。
  其特点是，在sql端方便组合，且能直接返回数据给客户端不必二次查询（注）
  在程序上仅需要修改对应的sql，但这对使用框架开发的程序很不方便，比如使用了ORM。
  另外还需要对mysql进行重新编译，且需要mysql-5.1以上版本
  支持插件存储。系统管理员可使用这种方式

>  
> 二次查询注：sphinx在检索到结果后只能返回记录的ID，而非要查的sql数据，故需要重新根据这些ID再次从数据库中查询  
>  


## sphinx 配置

* charset_table  字符表，sphinx会对中文进行单字切分 即进行字索引，若要使用中文分词，必须使用其他分词插件
* ngram_chars 加上这个选项，则会对每个中文，英文字词进行分割，速度会慢
* ngram_len  对于非字母型数据的长度切割
* min_infix_len  最小中缀
* min_prefix_len  最小前缀
* charset_type  数据编码
* min_word_len   索引的词最小长度
* seamless_rotate  是否支持无缝切换，做增量索引时通常需要
* max_matches  查询结果的最大返回数

## sphinx 问题

```
ERROR: index ‘product’: raw_hits: write error: 122070 of 262017 bytes written
```

此类问题是索引写入磁盘错误导致，有多个原因。  
注意查看磁盘空间是否已满。  
另外，还可能是因为是否有多个indexer进程在进行，写入索引失败！  

还有个解决方法是：减少 indexer配置中 max_iosize的大小。  
max_iosize是sphinx最大允许的I/O操作大小，以字节为单位，用于I/O节流。  
比如可以设置为 524288（512KB）

1、增量索引，注意删除的问题  
2、对大数据，一定要给sphinx数据目录留出大量空间，因为临时文件会占据非常大的空间


sphinx在rotate时出现以下问题。    
(searchd.log)   

```
WARNING: rotating index ‘sphinx’: prealloc: mmap() failed: Cannot allocate memory (length=431854320); using old index
```

同时，在索引数据目录中会出现sphinx.spl sphinx.new.spl的情况，导致原来的索引不能正确的检索到  

sphinx indexer有2个进程同时在运行，sphinx 的indexer不能同时使用，导致无法分配内存。并使indexer使用旧的索引文件  

先了解一下sphinx的 –rotate机制：  

indexer完成索引->发送SIGHUP 给searchd（同时在终端输出索引已经完成）->searchd接到中断信号->等待所有子进程退出->重命名 当前索引为旧索引为 .old->重命名 .new 索引文件作为当前索引->尝试加载当前索引文件->如果加载失败，searchd会把.old文件回滚为当前文件，并把刚建立的新索引重命名 为 .new->加载成的话：完成无缝衔接  

执行 rotate开关情况下，indexer在完成索引后会首先会发送一个中断信号给searchd（并且会输出已经索引完成）。  

接着 searchd会做以下事情：  

1）等待所有子进程退出  
2）重命名 当前索引为旧索引为 .old
3）重命名 .new 索引文件作为当前索引
4）尝试加载当前索引文件
5）如果加载失败，searchd会把.old文件回滚为当前文件，并把刚建立的新索引重命名为 .new

鉴于以上情况，很可能是开启了2个检测目录访问权限的进程。用户同时使用2个indexer且 searchd运行其下 等等  



sphinx的searchd在启动时会创建一个 .spl 锁文件，并在关闭时会删除它。在indexer创建索引时如果发现有 .spl文件，则不会创建新索引，除非使用 –rotate  

所以，出现这样的问题可能是 锁文件不知咋的就丢失啦，或者重建索引时没有使用 –rotate开关  

具体操作：

killall searchd 然后重启。重启后会自动加载重命名 sphinx.new.sp*为 sphinx.sp*  

另外，出现这样的问题时，最好注意 –rotate的使用，在应用许可 的情况下，不妨直接采用 关闭searchd 再索引，然后再开启 searchd  


关于updateAttribute更新索引的问题  

sphinx使用api不能马上真正的更新索引，但更新后api能显示索引已经是更新了。不过使用cli端的search就不能搜索到。只有在searchd重启后才会写入磁盘文件中。切记！  



Sphinx 怎样针对字段搜索  

co_do是要检索的字段 注意，要使用多字段搜索，必须使用 SPH_MATCH_EXTENDED2 模式，即 $cl->SetMatchMode(SPH_MATCH_EXTENDED); //使用多字段模式，这是必须！扩展模式 $res = $cl->Query(“@co_do $q”, $index,’非常好’);  


sphinx排序问题  

$sphinx->SetSortMode(SPH_SORT_EXTENDED,’status DESC,is_deleted DESC’); //组内排序 setGroupBy排序的话，分成组间排序和组内排序，比如：（317，1，hello）,(317,0,world)。如果组内排序的话，需先使用SetSortMode(),进行自然排序，然后 使用group排序，这样在组间排序和组内排序都成自然状态了！  



Q、WARNING: maxed out, dismissing client  
这是sphinx 客户端找不到searchd守护进程。具体可能是索引的锁文件了 (***.spl)丢失，  这个文件通常是用来标识searchd是否开启。  
通常客户端也会返回“zero-sized searchd response”。  解决办法：  重启searchd即可    


