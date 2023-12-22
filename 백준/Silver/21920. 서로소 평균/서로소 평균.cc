#include <iostream>
using namespace std;

int gcd(int a, int b) {
    if (a < b) {
        int c = a;
        a = b;
        b = c;
    }

    while (b > 0) {
        int c = a;
        a = b;
        b = c % b;
    }

    return a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int numbers[500001];
    double coprimesSum = 0;
    int coprimesCount = 0;

    int N;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        cin >> numbers[i];
    }

    int X;
    cin >> X;

    for (int i = 0; i < N; ++i) {
        int coprime = gcd(numbers[i], X);

        if (coprime == 1) {
            coprimesSum += numbers[i];
            coprimesCount++;
        }
    }

    cout << coprimesSum / coprimesCount;
    
    return 0;
}