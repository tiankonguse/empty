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
struct handler_base {
    virtual _R operator() ( _P1 ) = 0;
};

template <typename _R, typename _P1, typename _FuncType>
class handler : public handler_base<_R, _P1> {
public:
    typedef _FuncType func_type;
public:
    handler( const func_type &func ) :
        _func( func ) {
    }

    _R operator() ( _P1 p ) {
        return _func( p );
    }

public:
    func_type _func;
};

template <typename _R, typename _P1>
class functor {
public:
    typedef handler_base<_R, _P1> handler_type ;
public:
    template <typename _FuncType>
    functor( _FuncType func ) :
        _handler( new handler<_R, _P1, _FuncType>( func ) ) {
    }

    ~functor() {
        delete _handler;
    }

    _R operator() ( _P1 p ) {
        return (*_handler)( p );
    }

private:
    handler_type *_handler;
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

void fivePointFun() {
    functor<int, int>cmd1( testPointFun );
    cmd1(1);

    Func obj;
    functor<int, int>cmd2(obj);
    cmd2( 2 );
}

int main() {
    fivePointFun();
    return 0;
}
