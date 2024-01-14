#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, B;
    cin >> N >> M >> B;

    int board[501][501];

    int min_height = 257;
    int max_height = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> board[i][j];
            min_height = min(min_height, board[i][j]);
            max_height = max(max_height, board[i][j]);
        }
    }

    int ans_height = 0;
    int ans_time = 1000000001;

    for (int height = min_height; height <= max_height; height++) {
        int left_block = B;
        int time = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] > height) {
                    time += 2 * (board[i][j] - height);
                    left_block += (board[i][j] - height);
                }

                if (board[i][j] < height) {
                    time += height - board[i][j];
                    left_block -= height - board[i][j];
                }
            }
        }

        if (left_block < 0) {
            continue;
        }

        if (time <= ans_time) {
            ans_time = time;
            ans_height = height;
        }
    }

    cout << ans_time << ' ' << ans_height;
    return 0;
}