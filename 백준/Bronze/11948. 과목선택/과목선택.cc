#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    int small = 101;
    for(int i = 0; i < 4; i++){
        int a;
        cin >> a;
        small = min(small, a);
        sum += a;
    }
    sum -= small;
    int a,b;
    cin >> a >> b;
    if(a > b){
        sum += a;
    }
    else {
        sum += b;
    }
    cout << sum;
}