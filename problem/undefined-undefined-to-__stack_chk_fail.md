# undefined reference to `__stack_chk_fail' 


编译一个程序的时候，　报　`undefined reference to `__stack_chk_fail' `错误，　网上查询了一下，　原来编译时少加了个参数。  


加上 `-fno-stack-protector` 参数即可。  



