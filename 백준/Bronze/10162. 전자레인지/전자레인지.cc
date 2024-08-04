#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    int a = 0, b = 0, c = 0;
    if (t >= 300) {
        a = t/300;
        t -= a*300;
    }

    if (t >= 60) {
        b = t/60;
        t -= b*60;
    }

    if (t >= 10) {
        c = t/10;
        t -= c*10;
    }

    if (t == 0) {
        printf("%d %d %d\n", a, b, c);
    }
    else {
        cout << -1 << endl;
    }

    return 0;
}