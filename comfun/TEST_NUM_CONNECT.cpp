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

#define EMPTY_PARAMS(...) EMPTY_PARAMS_OUTER(__VA_ARGS__, EMPTY_PARAMS_EXTEND())
#define EMPTY_PARAMS_OUTER(...) EMPTY_PARAMS_INTER(__VA_ARGS__)
#define EMPTY_PARAMS_INTER( _1, _2, _3, _4, _5, _6, _7, _8, _9,_10, _11,_12,_13,_14,_15,_16, N, ...) N
#define EMPTY_PARAMS_EXTEND() 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0

#define STRING(s) REAL_STRING(s)
#define REAL_STRING(s) #s

#define CONNECT(a, b) REAL_CONNECT(a,b)
#define REAL_CONNECT(a,b) a##b

#define TEST_NUM1(a) a
#define TEST_NUM2(a,b)  CONNECT(a, b)
#define TEST_NUM3(a,b,c) CONNECT(TEST_NUM2(a,b), c)


#define TEST_NUM(...) TEST_NUM_N(NUM_PARAMS(__VA_ARGS__), __VA_ARGS__)
#define TEST_NUM_N(n,...) TEST_NUM_N_FIX(n, __VA_ARGS__)
#define TEST_NUM_N_FIX(n, ...) TEST_NUM##n(__VA_ARGS__)

int main() {
   printf("%s\n",STRING(TEST_NUM(1,2)));
    return 0;
}
