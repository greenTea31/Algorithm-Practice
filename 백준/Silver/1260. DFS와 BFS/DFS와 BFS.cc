#include <iostream>
#include <algorithm>
#include <cstring>
#include <stack>
#include <queue>
using namespace std;

bool visited[1001];
vector<int> v[1001];
stack<int> st;

void dfs(int start) {
    visited[start] = true;
    cout << start << " ";

    for (int nxt : v[start]) {
        if (visited[nxt]) continue;
        dfs(nxt);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, V;
    cin >> N >> M >> V;

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    for (int i = 0; i < N+1; i++) {
        sort(v[i].begin(), v[i].end());
    }

    dfs(V);
    cout << '\n';
    memset(visited, 0, sizeof(visited));

    queue<int> q;
    q.push(V);
    cout << V;
    visited[V] = true;

    while (!q.empty()) {
        int cur = q.front(); q.pop();
        for (int nxt : v[cur]) {
            if (visited[nxt]) continue;
            visited[nxt] = true;
            cout << " " << nxt;
            q.push(nxt);
        }
    }

    return 0;
}