
#include <iostream>
#include<queue>
using namespace std;

int n, k;

int main()
{
    cin >> n >> k;
    queue<int> q;
    for (int i = 1; i <= n; i++) {
        q.push(i);
    }
    int cnt = 1;
    cout << '<';
    while (!q.empty()) {
        if (cnt++ % k == 0) {
            cout << q.front(); q.pop();
            if (!q.empty()) {
                cout << ',' << ' ';
            }
        }
        else {
            q.push(q.front());
            q.pop();
        }
    }
    cout << '>';
}