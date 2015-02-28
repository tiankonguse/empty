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


void wantPointFun() {
    PointFun pointFunOne = testPointFun;
    pointFunOne(6);

    PointFun pointFunTwo = testPointFunTwo;
    pointFunTwo(7,7);

    printf("end  wantPointFun\n\n");
}



int main() {
    wantPointFun();

    return 0;
}
