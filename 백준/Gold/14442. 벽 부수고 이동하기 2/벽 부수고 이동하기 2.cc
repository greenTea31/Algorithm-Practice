#include <iostream>
#include <queue>
#include <array>
#define MAX_DIST 1000005;
using namespace std;

struct Dot {
    int locate[2];
    int destroy;
};

int visited[1001][1001][11];
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int i = 0; i < 1001; i++) {
        for (int j = 0; j < 1001; j++) {
            for (int k = 0; k < 11; k++) {
                visited[i][j][k] = MAX_DIST;
            }
        }
    }

    int N, M, K;
    cin >> N >> M >> K;
    string map[1001];

    for (int i = 0; i < N; i++) {
        cin >> map[i];
    }

    visited[0][0][0] = 0;
    queue<Dot> q;
    q.push({{0, 0}, 0});

    while (!q.empty()) {
        Dot cur = q.front(); q.pop();

        for (int i = 0; i < 4; i++) {
            int ny = cur.locate[0] + dy[i];
            int nx = cur.locate[1] + dx[i];
            if (ny < 0 || ny >= N || nx < 0 || nx >= M) continue;
            if (map[ny][nx] == '1') {
                if (cur.destroy >= K) continue;
                int temp = visited[ny][nx][cur.destroy+1];
                if (temp <= visited[cur.locate[0]][cur.locate[1]][cur.destroy] + 1) continue;
                visited[ny][nx][cur.destroy+1] = visited[cur.locate[0]][cur.locate[1]][cur.destroy] + 1;
                q.push({{ny, nx}, cur.destroy+1});
            } else {
                int temp = visited[ny][nx][cur.destroy];
                if (temp <= visited[cur.locate[0]][cur.locate[1]][cur.destroy] + 1) continue;
                visited[ny][nx][cur.destroy] = visited[cur.locate[0]][cur.locate[1]][cur.destroy] + 1;
                q.push({{ny, nx}, cur.destroy});
            }
        }
    }

    int ans = MAX_DIST;

    for (int i = 0; i <= K; i++) {
        if (visited[N-1][M-1][i] < ans) ans = visited[N-1][M-1][i];
    }

    if (ans == 1000005) ans = -2;
    cout << ans+1;

    return 0;
}