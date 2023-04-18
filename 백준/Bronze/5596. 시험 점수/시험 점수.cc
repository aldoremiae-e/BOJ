#include <iostream>
using namespace std;

int q,w,e,r;
int a,s,d,f;

int main(){
    cin >> q >> w >> e >> r;
    cin >> a >> s >> d >> f;
    int sum1 = q + w + e + r;
    int sum2 = a + s + d + f;
    cout << max(sum1, sum2);
}