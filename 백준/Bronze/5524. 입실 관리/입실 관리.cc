#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    while(n--){
        string s;
        cin >> s;
        for(int j = 0; j < s.size(); j++){
            if(s[j] >= 'A' && s[j] <= 'Z'){
                s[j] = s[j] - 'A' + 'a';
            }
        }
        cout << s << '\n';
    }
}