#include <iostream>
#include <queue>
#include <array>
#include <vector>
#include <algorithm>
#define MAXIMUM_CITY 300001
using namespace std;

bool visited[MAXIMUM_CITY];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, K, X;
    cin >> N >> M >> K >> X;

    vector<int> v[MAXIMUM_CITY];
    vector<int> answerList;

    for (int i = 0; i < M; i++) {
        int A, B;
        cin >> A >> B;
        v[A].push_back(B);
    }

    queue<array<int, 2>> q;
    q.push({0, X});
    visited[X] = true;

    while (!q.empty()) {
        array<int, 2> cur = q.front(); q.pop();

        for (int nxt : v[cur[1]]) {
            if (visited[nxt]) continue;

            visited[nxt] = true;

            if (cur[0] + 1 == K) {
                answerList.push_back(nxt);
                continue;
            }
            
            q.push({cur[0]+1, nxt});
        }
    }

    sort(answerList.begin(), answerList.end());

    if (answerList.empty()) {
        cout << -1;
    } else {
        for (int ans : answerList) {
            cout << ans << '\n';
        }
    }

    return 0;
}