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



template <typename _T, typename _U>
struct type_list {
    typedef _T head_type;
    typedef _U tail_type;
};

#define TYPE_LIST1( T1 ) type_list<T1, null_type>
#define TYPE_LIST2( T1, T2 ) type_list<T1, TYPE_LIST1( T2 )>
#define TYPE_LIST3( T1, T2, T3 ) type_list<T1, TYPE_LIST2( T2, T3 )>

template <typename _R, typename _ParamList>
struct handler_base;

struct null_type { };

template <typename _R>
struct handler_type_base {
    typedef _R result_type;
    typedef null_type param1_type;
    typedef null_type param2_type;
};

template <typename _R>
struct handler_base<_R, void> : public handler_type_base<_R> {
    virtual _R operator() ( void ) = 0;
};

template <typename _R, typename _P1>
struct handler_base<_R, TYPE_LIST1( _P1 )> : public handler_type_base<_R> {
    typedef _P1 param1_type;

    virtual _R operator() ( _P1 ) = 0;
};

template <typename _R, typename _P1, typename _P2>
struct handler_base<_R, TYPE_LIST2(_P1, _P2 )> : public handler_type_base<_R> {
    typedef _P1 param1_type;
    typedef _P2 param2_type;

    virtual _R operator() ( _P1, _P2 ) = 0;
};

template <typename _R, typename _ParamList, typename _FuncType>
class handler : public handler_base<_R, _ParamList> {
public:
    typedef _FuncType func_type;

    typedef handler_base<_R, _ParamList> base_type;
    typedef typename base_type::param1_type param1_type;
    typedef typename base_type::param2_type param2_type;

public:
    handler( const func_type &func ) :
        _func( func ) {
    }

    _R operator() () {
        return _func();
    }

    _R operator() ( param1_type p ) {
        return _func( p );
    }

    _R operator() ( param1_type p1,param2_type p2 ) {
        return _func( p1, p2 );
    }
public:
    func_type _func;
};

/// functor
template <typename _R, typename _ParamList>
class functor {
public:
    typedef handler_base<_R, _ParamList> handler_type ;

    typedef typename handler_type::param1_type param1_type;
    typedef typename handler_type::param2_type param2_type;

public:
    template <typename _FuncType>
    functor( _FuncType func ) :
        _handler( new handler<_R, _ParamList, _FuncType>( func ) ) {
    }

    ~functor() {
        delete _handler;
    }

    _R operator() () {
        return (*_handler)();
    }

    _R operator() ( param1_type p ) {
        return (*_handler)( p );
    }
    _R operator() ( param1_type p1 ,param2_type p2 ) {
        return (*_handler)( p1, p2 );
    }

private:
    handler_type *_handler;
};

int testPointFun(int num) {
    printf("testPointFun %d\n",num);
    return 0;
}
int testPointFunTwo(int one, int two) {
    printf("testPointFunTwo %d\n",one+two );
    return 0;
}


struct Func {
    int operator() ( int num ) {
        printf("Func class %d\n",num);
        return num;
    }
};

void sixPointFun() {
    functor<int, TYPE_LIST1(int)>cmd1( testPointFun );
    cmd1(1);

    Func obj;
    functor<int, TYPE_LIST1(int)>cmd2(obj);
    cmd2( 2 );

    functor<int, TYPE_LIST2(int,int)>cmd3( testPointFunTwo );
    cmd3(1,2);
}

int main() {
    sixPointFun();
    return 0;
}
