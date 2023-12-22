#include <iostream>
#include <vector>
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

    vector<int> numbers;

    double coprimesSum = 0;
    int coprimesCount = 0;

    int N;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        int num;
        cin >> num;
        numbers.push_back(num);
    }

    int X;
    cin >> X;

    for (int num : numbers) {
        int coprime = gcd(num, X);

        if (coprime == 1) {
            coprimesSum += num;
            coprimesCount++;
        }
    }

    cout << coprimesSum / coprimesCount;

    return 0;
}