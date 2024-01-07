#include <iostream>
#include <string>
using namespace std;

const int MAX_VALUE = 2501;
string board[51];

int getWBBoard(int r, int c) {
    int more = 0;

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if ((i+j) % 2 == 0 && board[r+i][c+j] != 'W') more++;
            if ((i+j) % 2 != 0 && board[r+i][c+j] != 'B') more++;
        }
    }

    return more;
}

int getBWBoard(int r, int c) {
    int more = 0;

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if ((i+j) % 2 != 0 && board[r+i][c+j] != 'W') more++;
            if ((i+j) % 2 == 0 && board[r+i][c+j] != 'B') more++;
        }
    }

    return more;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        cin >> board[i];
    }

    int ans = MAX_VALUE;

    for (int i = 0; i < N-7; i++) {
        for (int j = 0; j < M-7; j++) {
            int WBMore = getWBBoard(i, j);
            int BWMore = getBWBoard(i, j );
            ans = ans > WBMore ? WBMore : ans;
            ans = ans > BWMore ? BWMore : ans;
        }
    }

    cout << ans;

    return 0;
}