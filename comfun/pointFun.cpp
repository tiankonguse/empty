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




void testPointFun(int num) {
    printf("testPointFun %d\n",num);
}

void testPointFunTwo(int num, int num2) {
    printf("testPointFunTwo %d %d\n",num, num2);
}

void pointFun() {
    void (*pFunOne)(int);
    pFunOne = testPointFun;
    pFunOne(1);

    void (*pFunTwo)(int) = testPointFun;
    pFunTwo(2);

    void (*pFunThree)(int)(testPointFun);
    pFunThree(3);

    typedef void (*PestPointFun)(int);
    PestPointFun pFunFour = testPointFun;
    pFunFour(4);

    typedef void (*PestPointFunTwo)(int, int);
    PestPointFunTwo pFunFive = testPointFunTwo;
    pFunFive(5,5);

    printf("end  pointFun\n\n");
}



int main() {
    pointFun();

    return 0;
}
