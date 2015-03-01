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





#define NUM_PARAMS(...) NUM_PARAMS_OUTER(__VA_ARGS__, NUM_PARAMS_EXTEND())
#define NUM_PARAMS_OUTER(...) NUM_PARAMS_INTER(__VA_ARGS__)
#define NUM_PARAMS_INTER( _1, _2, _3, _4, _5, _6, _7, _8, _9,_10, _11,_12,_13,_14,_15,_16, N, ...) N
#define NUM_PARAMS_EXTEND() 16,15,14,13,12,11,10, 9,8,7,6,5,4,3,2,1,0


#define TYPE_LIST1( T1 ) type_list<T1, null_type>
#define TYPE_LIST2( T1, T2 ) type_list<T1, TYPE_LIST1( T2 )>
#define TYPE_LIST3( T1, T2, T3 ) type_list<T1, TYPE_LIST2( T2, T3 )>

#define TYPE_LIST_N(n,...) TYPE_LIST#n(__VA_ARGS__)
#define TYPE_LIST(...) TYPE_LIST_N(NUM_PARAMS(__VA_ARGS__), __VA_ARGS__)


#define TEST_NUM3(a,b,c) printf("%d %d %d\n", a,b,c)
#define TEST_NUM2(a,b) printf("%d %d \n", a,b)
#define TEST_NUM1(a) printf("%d\n", a)

#define TEST_NUM(...) TEST_NUM_N(NUM_PARAMS(__VA_ARGS__), __VA_ARGS__)
#define TEST_NUM_N(n,...) TEST_NUM_N_FIX(n, __VA_ARGS__)
#define TEST_NUM_N_FIX(n,...) TEST_NUM##n(__VA_ARGS__)

#define PP_NARG(...) PP_NARG_(__VA_ARGS__, PP_RSEQ_N())
#define PP_NARG_(...) PP_ARG_N(__VA_ARGS__)
#define PP_ARG_N( \
_1, _2, _3, _4, _5, _6, _7, _8, _9,_10, \
_11,_12,_13,_14,_15,_16, N, ...) N
#define PP_RSEQ_N() \
16,15,14,13,12,11,10, \
9,8,7,6,5,4,3,2,1,0

int main() {
    printf("%d",PP_NARG());
    return 0;
}
