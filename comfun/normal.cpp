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





void normal() {
    int one = 1;
    int* pOne;
    pOne = &one;
    printf("pOne %d\n", *pOne);

    int two = 2;
    int* pTwo= &two;
    printf("pTwo %d\n", *pTwo);

    int three = 3;
    int* pThree(&three);
    printf("pThree %d\n", *pThree);

    printf("end normal\n\n");
}


int main() {
    normal();

    return 0;
}
