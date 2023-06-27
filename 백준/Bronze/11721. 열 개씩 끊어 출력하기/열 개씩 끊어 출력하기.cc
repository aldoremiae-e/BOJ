#include<iostream>
using namespace std;

string s;

int main(){
    cin >> s;
    int index = 0;
    while(index < s.size()){
        for(int i = 0; i < 10; i++){
            if(index + i == s.size()) break;
            cout << s[index + i];
        }
        index += 10;
        cout << '\n';
    }
}