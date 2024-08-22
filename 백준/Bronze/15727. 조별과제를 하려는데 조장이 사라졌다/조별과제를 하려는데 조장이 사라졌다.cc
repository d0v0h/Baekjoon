#include<iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    int result = 0;
    while (t > 0) {
        if (t >= 5) {
            t -= 5;
            result += 1;
        }
        else if (t >= 4) {
            t -= 4;
            result += 1;
        }
        else if (t >= 3) {
            t -= 3;
            result += 1;
        }
        else if (t >= 2) {
            t -= 2;
            result += 1;
        }
        else {
            t -= 1;
            result += 1;
        }
    }

    printf("%d\n", result);
    return 0;
}