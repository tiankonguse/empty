# 检查数据是否在指定数据集合中

方案1：  

申请512M的内存，一个bit位代表一个unsigned int值。  

读入40亿个数，设置相应的bit位，读入要查询的数，查看相应bit位是否为1，为1表示存在，为0表示不存在。  


方案2：  

这个问题在《编程珠玑》里有很好的描述，大家可以参考下面的思路，探讨一下：  

又因为2^32为40亿多，所以给定一个数可能在，也可能不在其中；  

这里我们把40亿个数中的每一个用32位的二进制来表示  

假设这40亿个数开始放在一个文件中。  

然后将这40亿个数分成两类:  

1. 最高位为0  
2. 最高位为1  

并将这两类分别写入到两个文件中，其中一个文件中数的个数<=20亿，而另一个>=20亿（这相当于折半了）；  

与要查找的数的最高位比较并接着进入相应的文件再查找  

再然后把这个文件为又分成两类:  

1. 次最高位为0  
2. 次最高位为1  

并将这两类分别写入到两个文件中，其中一个文件中数的个数<=10亿，而另一个>=10亿（这相当于折半了）；  

与要查找的数的次最高位比较并接着进入相应的文件再查找。  
.......  
以此类推，就可以找到了,而且时间复杂度为O(logn)，方案2完。  

附：这里，再简单介绍下，位图方法：  

使用位图法判断整形数组是否存在重复   

判断集合中存在重复是常见编程任务之一，当集合中数据量比较大时我们通常希望少进行几次扫描，这时双重循环法就不可取了。  

位图法比较适合于这种情况，它的做法是按照集合中最大元素max创建一个长度为max+1的新数组，然后再次扫描原数组，遇到几就给新数组的第几位置上1，如遇到5就给新数组的第六个元素置1，这样下次再遇到5想置位时发现新数组的第六个元素已经是1了，这说明这次的数据肯定和以前的数据存在着重复。这种给新数组初始化时置零其后置一的做法类似于位图的处理方法故称位图法。  

它的运算次数最坏的情况为2N。  

如果已知数组的最大值即能事先给新数组定长的话效率还能提高一倍。  

 
