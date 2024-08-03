#include<iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    int a, b;
    for (int i = 0; i < t; i++) {
        cin >> a >> b;
        printf("Case %d: %d\n", i+1, a+b);
    }
    return 0;
}