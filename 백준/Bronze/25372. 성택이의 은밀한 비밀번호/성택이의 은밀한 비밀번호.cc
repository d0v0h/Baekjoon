#include<iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i=0; i<t ;i++) {
        string password;
        cin >> password;
        if (password.length() >= 6 && password.length() <= 9) {
            cout << "yes" << endl;
        }
        else {
            cout << "no" << endl;
        }
    }
}