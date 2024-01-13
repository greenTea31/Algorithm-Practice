#include <iostream>
#include <algorithm>
using namespace std;

int customRound(double num) { // 13.24
    if ((int) (num * 10) % 10 >= 5) {
        return (int) num + 1;
    } else {
        return (int) num;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    
    if (n == 0) {
        cout << 0;
        return 0;
    }
    
    int diffcult[300001];

    for (int i = 0; i < n; i++) {
        cin >> diffcult[i];
    }

    sort(diffcult, diffcult+n);

    int julsa = customRound(n * 0.15);
    int sum = 0;

    for (int i = julsa; i < n - julsa; i++) {
        sum += diffcult[i];
    }

    cout << customRound(sum / (double) (n - (julsa * 2)));
    return 0;
}