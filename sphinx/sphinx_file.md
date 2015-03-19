# sphinx数据文件简析

Sphinx使用的文件包括 “sph”， “spa”， “spi”， “spd”, “spp”， “spm” ，还有锁文件（.spl）。其中sph是系统的配置文件。其它则为索引文件。

l Spi 文件：保存WordId及指向此WordId对应的文档信息在spd文件的指针。Spi文件在检索程序启动时完全加载入内存。Spi文件是分块的，块内排序，块之间也排序。分块的目的应该是为了快速检索到WordId，因为Spi中的WordId是变长压缩的，索引需要先在块级别做二分定位，再在快内解压缩查找。


文件结构，每块中结构，wordId实际存储的是差值

    WordId    SpdFilePointer    DocNum    HitNum

2 Spd文件：
文件结构

    DocID    [DocInfo]    HitFilePointer    FieldNum    HitNum

3 Spp文件
文件结构

    HitPos

4 Spa文件：存储DocInfo的文件，检索程序启动时会把此文件加载如内存，sphinx可以指定DocInfo的存储方式，
① 存储到spd文件中（InLine）
②. 另外单独存储。指定此，就会生成spa文件
文件结构：

    DocId    DocInfo

5 Spm文件：在DocInfo中，有一种特殊的属性，叫MVA，多值属性。Sphinx对此属性特殊处理，需要存储在spm文件中。检索程序启动时会把此文件加载如内存。此（MVA）属性在DocInfo对应位置存储其在此文件中的字节偏移量。
文件结构：

    DocId   Anum,A1,A2,…,An    Bnum,B1,B2,…,Bn    …

由于在第一趟扫描过程中会出现WordID相同的不同Hits(不同文档或者不同位置不同字段)，二趟前会根据WordID排序，WordID相同的Hits会连续出现并合并(合并到第一次出现的相同WordID中)
