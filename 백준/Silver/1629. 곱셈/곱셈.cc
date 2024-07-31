#include <iostream>
using namespace std;

long long a, b, c;

long long modulo(long long a, long long b, long long c){
    if (b == 0) {
        return 1 % c;
    }
    else if (b == 1) {
        return a % c;
    }
    else if (b % 2 == 0) {
        long long result = modulo(a, b / 2, c);
        return (result * result) % c;
    }
    else {
        long long result = modulo(a, b / 2, c);
        return ((result * result % c) * (a % c)) % c;
    }
}

int main() {
    cin >> a >> b >> c;
    cout << modulo(a, b, c) << endl;
    return 0;
}