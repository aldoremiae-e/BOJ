#include<iostream>
using namespace std;

int q,w,e,a,s,d;

int main(){
    cin >> q >> w >> e >> a >> s >> d;
    int z = q * 3 + w * 2 + e;
    int x = a * 3 + s * 2 + d;
    if(z > x){
        cout << 'A';
    }
    else if(x > z){
        cout << 'B';
    }
    else{
        cout << 'T';
    }
}