#include <iostream>
using namespace std;

int main(){
    int n, A, B, C;
    cin >> n;

    cin >> A >> B >> C;

    int result = ( A > n ? n : A) + ( B > n ? n : B) + ( C > n ? n : C);
    cout << result << endl;
}