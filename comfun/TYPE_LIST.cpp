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


#define TYPE_LIST(...) TYPE_LIST_N(NUM_PARAMS(__VA_ARGS__), __VA_ARGS__)
#define TYPE_LIST_N(n,...) TYPE_LIST_N_FIX(n, __VA_ARGS__)
#define TYPE_LIST_N_FIX(n, ...) TYPE_LIST##n(__VA_ARGS__)

#define TYPE_LIST0(...) null_type
#define TYPE_LIST1(T1, ... ) type_list<T1, TYPE_LIST_HELP(NUM_PARAMS(__VA_ARGS__),__VA_ARGS__)>
#define TYPE_LIST_HELP(n,...) TYPE_LIST_HELP_FIX(n, __VA_ARGS__)
#define TYPE_LIST_HELP_FIX(n, ...)  TYPE_LIST(__VA_ARGS__)



int main() {

    return 0;
}
