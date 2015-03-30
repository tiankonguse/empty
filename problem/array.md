# 数组算法面试题

T( 0 ) = 1 ; 
T(1)=1;
T(2)=2;
T(n)=T(n-1)+T(n-2)+T(n-3);

用最优方式求T(n) ;

```
int T(int n) {

}
```

## 非递归

```
def t(n, T=[0,1,2]):
  if len(T) > n: 
    return T[n]
  else:
    for i in range(3,n+1):
      T.append(T[-1]+T[-2]+T[-3])
    return T[n]
 
if __name__ == "__main__":
  print t(50);
  print t(5);
```

## 递归版

```
def t(n):
   def t_iter(r, n):
       return r if n == 1 else t_iter([r[1], r[2], r[0] + r[1] + r[2]], n-1)
   return t_iter([0, 1, 2], n)
```


