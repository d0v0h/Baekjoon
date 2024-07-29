#include <iostream>
using namespace std;

int calc(int person, int n) {
    if (person > n) {
        return n;
    }
    else {
        return person;
    }
}

int main(){
    int n, A, B, C;
    cin >> n;

    cin >> A >> B >> C;

    int result = 0;

    result += calc(A, n);
    result += calc(B, n);
    result += calc(C, n);

    cout << result << endl;

    return 0;
}