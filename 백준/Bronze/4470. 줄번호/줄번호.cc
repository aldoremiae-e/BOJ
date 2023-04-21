#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore();
    for(int i = 0; i < n; i++){
        string s;
        getline(cin,s);
        cout << i + 1 << ". " << s << '\n';
    }
}