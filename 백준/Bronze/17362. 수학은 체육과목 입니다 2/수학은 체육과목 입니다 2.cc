#include<iostream>
using namespace std;

int n;

int main(){
    cin >> n;
    n %= 8;
    if(n == 1) cout << 1;
    else if(n == 2) cout << 2;
    else if(n == 3) cout << 3;
    else if(n == 4) cout << 4;
    else if(n == 5) cout << 5;
    else if(n == 6) cout << 4;
    else if(n == 7) cout << 3;
    else if(n == 0) cout << 2;
}