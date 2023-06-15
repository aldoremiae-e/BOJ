#include<iostream>
using namespace std;

int T;

int main(){
    cin >> T;
    while(T--){
        string s;
        cin >> s;
        int c = s[0] + s[2] - '0' - '0';
        cout << c << '\n';
    }
}