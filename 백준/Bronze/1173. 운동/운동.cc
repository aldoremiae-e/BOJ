#include <iostream>
using namespace std;

int N, m, M, T, R;

int main(){
    cin >> N >> m >> M >> T >> R;
    // 진짜시간, 운동시간
    // 쉬면  x 운동하면 운동시간 - 
    int time = 0;
    int realm = m;
    if (m+T > M){
        cout << -1;
        return 0;
    }
    while (1){
        if (N == 0) break;
        time++; //진짜시간 추가
        if ((realm+T) <= M){
            // 운동
            N--;
            realm = realm+T;
            continue;
        }
        else{
            // 휴식
            realm = realm-R;
            if (realm < m){
                realm = m;
            } 
            continue;
        }
    }
    cout <<time;
    return 0;
}