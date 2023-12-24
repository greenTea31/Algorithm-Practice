#include <iostream>
#include <array>
#include <vector>
#include <queue>
using namespace std;

bool visited[501];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> v[501];

    int n, m;
    cin >> n >> m;

    int ans = 0;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;

        v[a].push_back(b);
        v[b].push_back(a);
    }

    queue<array<int, 2>> q;
    visited[1] = true;
    q.push({1, 0});

    while (!q.empty()) {
        array<int, 2> cur = q.front(); q.pop();

        for (int nxt : v[cur[0]]) {
            if (visited[nxt] || cur[1] >= 2) continue;
            visited[nxt] = true;
            ans++;
            q.push({nxt, cur[1]+1});
        }
    }

    cout << ans;

    return 0;
}