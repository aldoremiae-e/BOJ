#include <iostream>

using namespace std;

int main()
{   
    int n;
    cin >> n;
    for (int i=0; i <n; i++){
        string num;
        cin >> num;
        if (num.size() >= 6 && num.size() <= 9){
            cout << "yes" << endl;
        }else{
            cout << "no" << endl;
        }
    }

    return 0;
}