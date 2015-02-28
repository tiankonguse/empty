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

template <typename _R, typename _P1>
class functor {
public:
    typedef _R (*func_type)( _P1 );
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
}


struct Func {
    int operator() ( int i ) {
        return i;
    }
};

void secondPointFun() {
    functor<int, int> cmd1( testPointFun );
    cmd1(1);

    Func obj;
    functor<int, int> cmd2(obj);
    cmd2( 2 );
}

int main() {
    secondPointFun();
    return 0;
}
