#  Python 过程式编程与函数式编程 


过程式与函数式是两种截然不同的编程方式和思考方法，下面以求解素数为例做一下对比。  

##  采用过程式编程 



```
def isPrime(n):
    mid = int(pow(n,0.5)+1)
    for i in xrange(2,mid):
        if n % i == 0 : 
            return False
        return True

primes=[]
for i in xrange(2,1000):
 if isPrime(i): primes += [i]
 print primes

```



##  采用函数式编程 



```
print reduce(lambda l,y:not 0 in map(lambda x:y % x, l) and l+[y] or l,xrange(2,1000), [] )
```



它同上面的算法是一样的，想看懂的话必须先知道map、reduce的用法，参考Python的官方文档，提示一下：l表示已经找到的素数序列，not 0 in map(lambda x:y %x,l) 表示数y能否被l中的任何一个数整除，继而返回l+\[y]或者l。  

对比一下这两段程序，可以明显地看出过程式的代码虽长但直白，适合初学算法的人，而函数式的代码短而晦涩，有着数学一样的抽象，适合hacker。但是如果你习惯了函数编程的思维方式，反而会觉得代码直观明了。不管采用哪种方式的编程，代码的可读性都是非常重要的，要根据具体的场合选用合适的编程方式。   


从效率的角度讲，一般函数式编程的效率会低一些。比如上面的例子，在确定一个数是不是质数时，过程式只要找到了一个它的因数就返回，而函数式需要除以比它小的所有质数，计算量要多一些。  

