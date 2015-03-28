# 搜索引擎与全文检索

这里对现有的开源的搜索引擎的一个简单介绍。

## [Lucene][lucene-org]

Lucene的开发语言是java, 也是java家族中最为出名的一个开源搜索引擎, 在java世界中已经是标准的全文检索程序, 它提供了完整的查询引擎和索引引擎, 没有中文分词引擎, 需要自己去实现, 因此用Lucene去做一个搜素引擎需要自己去架构.  

另外它不支持实时搜索, 但linkedin和twitter有分别对Lucene改进的实时搜素.   

其中Lucene有一个C++移植版本叫[CLucene][clucene-org], CLucene因为使用C++编写, 所以理论上要比lucene快.  



## [Sphinx][sphinxsearch]

Sphinx是一个用C++语言写的开源搜索引擎,也是现在比较主流的搜索引擎之一, 在建立索引的事件方面比Lucene快50%, 但是索引文件比Lucene要大一倍, 因此Sphinx在索引的建立方面是空间换取事件的策略, 在检索速度上, 和lucene相差不大, 但检索精准度方面Lucene要优于Sphinx,另外在加入中文分词引擎难度方面, Lucene要优于Sphinx.其中Sphinx支持实时搜索, 使用起来比较简单方便.  


对于中文分词，我们一般使用 [coreseek][coreseek] 和 [sfc][sphinx-for-chinese].  



## [Xapian][xapian]

Xapian是一个用C++编写的全文检索程序,它的api和检索原理和lucene在很多方面都很相似, 算是填补了lucene在C++中的一个空缺.  


## [Nutch][nutch-org]

Nutch是一个用java实现的开源的web搜索引擎, 包括爬虫crawler, 索引引擎,查询引擎. 其中Nutch是基于Lucene的, Lucene为Nutch提供了文本索引和搜索的API.  

对于应该使用Lucene还是使用Nutch,应该是如果你不需要抓取数据的话, 应该使用Lucene, 最常见的应用是: 你有数据源, 需要为这些数据提供一个搜索页面, 在这种情况下, 最好的方式是直接从数据库中取出数据, 并用Lucene API建立索引.  


## [DataparkSearch][dataparksearch]

DataparkSearch是一个用C语言实现的开源的搜索引擎. 其中网页排序是采用神经网络模型.  其中支持HTTP, HTTPS, FTP,NNTP等下载网页.包括索引引擎, 检索引擎和中文分词引擎(这个也是唯一的一个开源的搜索引擎里有中文分词引擎).能个性化定制搜索结果, 拥有完整的日志记录.   


## [Zettair][zettair-org]

Zettair是根据Justin Zobel的研究成果为基础的全文检索实验系统.它是用C语言实现的. 其中Justin Zobel在全文检索领域很有名气, 是业界第一个系统提出倒排序索引差分压缩算法的人, 倒排列表的压缩大大提高了检索和加载的性能, 同时空间膨胀率也缩小到相当优秀的水平. 由于Zettair是源于学术界, 代码是由RMIT University的搜索引擎组织写的, 因此它的代码简洁精炼, 算法高效, 是学习倒排索引经典算法的非常好的实例. 其中支持linux, windows, mac os等系统.  


## [Indri][indri-org]

Indri是一个用C语言和C++语言写的全文检索引擎系统, 是由University of Massachusetts和Carnegie Mellon University合作推出的一个开源项目. 特点是跨平台, API接口支持Java, PHP, C++.  


## [Terrier][terrier-org]

Terrier是由School of Computing Science, Universityof Glasgow用java开发的一个全文检索系统.  

## [Galago][galagosearch-org]

Galago是一个用java语言写的关于文本搜索的工具集. 其中包括索引引擎和查询引擎, 还包括一个叫TupleFlow的分布式计算框架(和google的MapReduce很像).这个检索系统支持很多Indri查询语言.  


## [Zebra][zebra-org]

Zebra是一个用C语言实现的检索程序, 特点是对大数据的支持, 支持EMAIL, XML, MARC等格式的数据.  

## [Solr][solr-org]

Solr是一个用java开发的独立的企业级搜索应用服务器, 它提供了类似于Web-service的API接口, 它是基于Lucene的全文检索服务器, 也算是Lucene的一个变种, 很多一线互联网公司都在使用Solr, 也算是一种成熟的解决方案.  


## [Elasticsearch][elasticsearch-org]

Elasticsearch是一个采用java语言开发的, 基于Lucene构造的开源, 分布式的搜索引擎. 设计用于云计算中, 能够达到实时搜索,稳定可靠. Elasticsearch的数据模型是JSON.  



## [Whoosh][whoosh-org]  

Whoosh是一个用纯python写的开源搜索引擎.  

## [Solandra][solandra-org]

Solandra 是一个实时的分布式搜索引擎，基于 Apache Solr 和 Apache Cassandra 构建。  

支持Solr的大多数默认特性 (search, faceting, highlights)  
数据复制，分片，缓存及压缩这些都由Cassandra来进行  
Multi-master (任意结点都可供读写)  
实时性高，写操作完成即可读到  
Easily add new SolrCores w/o restart across the cluster 轻松添加及重启结点  


## [IndexTank][indextank-engine]

IndexTank是一套基于Java的索引-实时全文搜索引擎实现.  

* 索引更新实时生效
* 地理位置搜索
* 支持多种客户端语言
* Ruby, Rails, Python, Java, PHP, .NET & more!
* 支持灵活的排序与评分控制
* 支持自动完成
* 支持面搜索（facet search）
* 支持匹配高亮
* 支持海量数据扩展（Scalable from a personal blog to hundreds of millions of documents! ）
* 支持动态数据

## [Compass][compass-project-org]

Compass是一个强大的,事务的,高性能的对象/搜索引擎映射(OSEM:object/search engine mapping)与一个Java持久层框架  

* 搜索引擎抽象层(使用Lucene搜索引荐)
* OSEM (Object/Search Engine Mapping) 支持
* 事务管理
* 类似于Google的简单关键字查询语言
* 可扩展与模块化的框架
* 简单的API

## [LIRE][lire-org]

LIRE是一款基于Java的图片搜索框架，其核心也是基于Lucene的，利用该索引就能够构建一个基于内容的图像检索(content- based image retrieval，CBIR)系统，来搜索相似的图像。  

## [Egothor][egothor-org]

Egothor是一个用Java编写的开源而高效的全文本搜索引擎。借助Java的跨平台特性，Egothor能应用于任何环境的应用，既可配置为单独的搜索引擎，又能用于你的应用作为全文检索之用。  


## 参考资料


* [调研 开源搜索引擎][xum2008-8740063]  
* [9个基于Java的搜索引擎框架][chuansong-695725]





[egothor-org]: http://www.egothor.org/cms/
[lire-org]: http://www.semanticmetadata.net/lire/
[compass-project-org]: http://www.compass-project.org/
[indextank-engine]: https://github.com/linkedin/indextank-engine
[solandra-org]: https://github.com/tjake/Solandra
[chuansong-695725]: http://chuansong.me/n/695725
[xum2008-8740063]: http://blog.csdn.net/xum2008/article/details/8740063
[whoosh-org]: https://bitbucket.org/mchaput/whoosh/wiki/Home
[elasticsearch-org]: http://www.elasticsearch.org/
[solr-org]: http://lucene.apache.org/solr/
[zebra-org]: https://www.indexdata.com/zebra
[galagosearch-org]: http://www.galagosearch.org/
[terrier-org]: http://terrier.org/
[indri-org]: http://www.lemurproject.org/indri/
[zettair-org]: http://www.seg.rmit.edu.au/zettair/index.html
[dataparksearch]: http://www.dataparksearch.org/
[nutch-org]: http://nutch.apache.org/
[xapian]: http://xapian.org/
[sphinxsearch]: http://sphinxsearch.com/
[coreseek]: http://www.coreseek.com/
[sphinx-for-chinese]: https://code.google.com/p/sphinx-for-chinese/
[clucene-org]: http://sourceforge.net/projects/clucene/
[lucene-org]: http://lucene.apache.org/


