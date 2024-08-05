#include <iostream>
using namespace std;

int main() {
    int h, w, n, m;
    cin >> h >> w >> n >> m;

    int a, b;
    if (h % (n+1) != 0) {
        a = h/(n+1);
        a += 1;
    }
    else {
        a = h/(n+1);
    }

    if (w % (m+1) != 0) {
        b = w/(m+1);
        b += 1;
    }
    else {
        b = w/(m+1);
    }
    cout << a*b << endl;
    return 0;
}