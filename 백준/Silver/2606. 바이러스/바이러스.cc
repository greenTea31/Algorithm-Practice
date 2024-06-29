#include <iostream>
#include <vector>
using namespace std;

vector<int> E[101];
bool visited[101];
int answer = -1;

void dfs(int x) {
    answer++;
    visited[x] = true;

    for (auto next : E[x]) {
        if (visited[next]) continue;
        dfs(next);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int computer, edge, u, v;
    cin >> computer;
    cin >> edge;

    for (int i = 0; i < edge; i++) {
        cin >> u >> v;
        E[u].push_back(v);
        E[v].push_back(u);
    }

    dfs(1);
    cout << answer << '\n';

    return 0;
}