#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    int edges[101][101];


    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> edges[i][j];
        }
    }

    for (int k = 0; k < N; k++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (edges[i][k] + edges[k][j] == 2) {
                    edges[i][j] = 1;
                }
            }
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << edges[i][j] << ' ';
        }
        cout << '\n';
    }

    return 0;
}