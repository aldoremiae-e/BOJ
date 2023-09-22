#include<iostream>
using namespace std;

int n;
char s;

int main(){
    cin >> n;
    int d = 0;
    int p = 0;
    for(int i = 0; i < n; i++){
        cin >> s;
        if(s == 'D'){
            d++;
        }
        else{
            p++;
        }
        if((d - p)*(p - d) == -4){
            cout << d << ':' << p;
            return 0;
        }
    }
    cout << d << ':' << p;
}