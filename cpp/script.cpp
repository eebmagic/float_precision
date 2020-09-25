#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    // cout << "test" << endl;
    // cout << bitset<32>(123) << " - " << 123 << endl;
    float end = 4294967296;
    for (float i = 0; i < end; i++) {
        cout << bitset<32>(i) << " - " << i << " - " << i / end << endl;
        // cout << bitset<32>(i) << " - " << i << endl;
    }
}
