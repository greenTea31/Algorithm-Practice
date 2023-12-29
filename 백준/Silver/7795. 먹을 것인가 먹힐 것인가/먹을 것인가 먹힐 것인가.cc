#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int tc = 0; tc < T; tc++) {
        int N, M;
        cin >> N >> M;

        int ans = 0;

        int A[20001], B[20001];

        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }

        for (int i = 0; i < M; i++) {
            cin >> B[i];
        }

        sort(A, A+N);
        sort(B, B+M);

        int aindex = 0;
        int bindex = 0;

        while (aindex < N && bindex < M) {
            if (A[aindex] <= B[bindex]) {
                aindex++;
            } else {
                ans += (N - aindex);
                bindex++;
            }
        }

        cout << ans << '\n';
    }

    return 0;
}