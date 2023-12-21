#include <iostream>
#define MAX 301
using namespace std;

long long pSum[MAX][MAX];
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            cin >> pSum[i][j];
            pSum[i][j] += pSum[i][j-1] +pSum[i-1][j]-pSum[i-1][j-1];
        }
    }

    int K;
    cin >> K;

    for (int a = 0; a < K; a++) {
        int i, j, x, y;
        cin >> i >> j >> x >> y;
        cout << pSum[x][y] - pSum[i - 1][y] - pSum[x][j - 1] + pSum[i - 1][j - 1] << '\n';
    }

    return 0;
}

