#include <iostream>

using namespace std;

int main()
{
    int a,b,c;
    cin >> a >> b >> c;
    int q,w,e;
    cin >> q >> w >> e;
    int z = b * 100 + c;
    int x = w * 100 + e;
    if(z > x) cout << q - a - 1 << '\n';
    else cout << q - a << '\n';
    cout << q - a + 1 << '\n';
    cout << q - a << '\n';
}