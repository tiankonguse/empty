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




#define EMPTY_PARAMS(...) EMPTY_PARAMS_OUTER( __VA_ARGS__, EMPTY_PARAMS_EXTEND())
#define EMPTY_PARAMS_OUTER(...) EMPTY_PARAMS_INTER(__VA_ARGS__)
#define EMPTY_PARAMS_INTER(  _0, _1, _2, _3, _4, _5, _6, _7, _8, _9,_10, _11,_12,_13,_14,_15,_16, N, ...) N
#define EMPTY_PARAMS_EXTEND() 2, 2,  2,  2,  2,  2,  2,  2,  2,  2,  2,   2,  2,  2,  2,  2,  1, 0




#define TEST_NUM(...) TEST_NUM_HELP(EMPTY_PARAMS(__VA_ARGS__), __VA_ARGS__)
#define TEST_NUM_HELP(n,...) TEST_NUM_HELP_FIX(n, __VA_ARGS__)
#define TEST_NUM_HELP_FIX(n,...) TEST_NUM##n(__VA_ARGS__)


#define CONNECT(a, b) a+b

#define TEST_NUM1(a) a
#define TEST_NUM2(a, ...) CONNECT(a, TEST_NUM(__VA_ARGS__))

int main() {


   printf("%d\n",TEST_NUM(1));
   // printf("%d\n",EMPTY_PARAMS(1,2,3,4));
    return 0;

}
