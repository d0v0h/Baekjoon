#include <iostream>
using namespace std;

int main(){
    string str;
    cin >> str;

    if (!str.compare("NLCS")) cout << "North London Collegiate School" << endl;
    else if (!str.compare("BHA")) cout << "Branksome Hall Asia" << endl;
    else if (!str.compare("KIS")) cout << "Korea International School" << endl;
    else if (!str.compare("SJA")) cout << "St. Johnsbury Academy" << endl;
    
    return 0;
}