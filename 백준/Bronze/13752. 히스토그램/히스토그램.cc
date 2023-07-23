#include<iostream>
using namespace std;

int n;

int main(){
    cin >> n;
    for (int i = 0; i < n; i++){
        int a;
        cin >> a;
        for(int j = 0; j < a; j++){
            cout << '=';
        }
        cout << '\n';
    }
}