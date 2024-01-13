#include <iostream>
#include <string>
using namespace std;

const int MOD = 1234567891;

long long pows(char a, long long b) {
    long long ret = (int) a - (int) 'a' + 1;

    if (b == 0) return ret;

    for (int i = 0; i < b; i++) {
        ret *= 31;
        ret %= MOD;
    }

    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int L;
    cin >> L;

    string s;
    cin >> s;

    long long sum = 0;

    for (int i = 0; i < L; i++) {
        sum += pows(s[i], i);
        sum %= MOD;
    }

    cout << sum;

    return 0;
}