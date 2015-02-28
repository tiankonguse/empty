#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<string>
#include<queue>
#include<map>
#include<cmath>
#include<stack>
#include<algorithm>
#include<functional>
#include<unistd.h>
#include <time.h>
#include<stdarg.h>
using namespace std;

template <typename _R, typename _P1,typename _FuncType>
class functor {
public:
    typedef _FuncType func_type;
public:
    explicit functor( const func_type &func ) :
        _func( func ) {
    }

    _R operator() ( _P1 p ) {
        return _func( p );
    }

private:
    func_type _func;
};

int testPointFun(int num) {
    printf("testPointFun %d\n",num);
    return 0;
}


struct Func {
    int operator() ( int num ) {
        printf("Func class %d\n",num);
        return num;
    }
};

void threePointFun() {
    functor<int, int, int (*)(int)> cmd1( testPointFun );
    cmd1(1);

    Func obj;
    functor<int, int, Func> cmd2(obj);
    cmd2( 2 );
}

int main() {
    threePointFun();
    return 0;
}
