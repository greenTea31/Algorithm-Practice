#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        int N;
        cin >> N;
        long long d[101];

        d[0] = 0; d[1] = 1; d[2] = 1; d[3] = 1; d[4] = 2; d[5] = 2;

        for (int i = 6; i <= N; i++) {
            d[i] = d[i-2] + d[i-3];
        }

        cout << d[N] << '\n';
    }

    return 0;
}