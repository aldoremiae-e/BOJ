#include<iostream>
#include<queue>
using namespace std;

int a,b,c;
priority_queue<int> pq;

int main(){
    cin >> a >> b >> c;
    pq.push(-a);
    pq.push(-b);
    pq.push(-c);
    cout << -pq.top() << ' '; pq.pop();
    cout << -pq.top() << ' '; pq.pop();
    cout << -pq.top() << ' '; pq.pop();
}