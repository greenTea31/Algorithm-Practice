#include <iostream>
#include <queue>
#include <vector>
#include <array>
#define MAX_N 50001
#define MAX_DIST 50000001
using namespace std;

struct compareArray {
    bool operator() (const array<int, 2>& a, const array<int, 2>& b) {
        return a[0] > b[0];
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    vector<array<int, 2>> v[MAX_N];

    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        int A, B, C;
        cin >> A >> B >> C;

        v[A].push_back({C, B});
        v[B].push_back({C, A});
    }

    priority_queue<array<int, 2>, vector<array<int, 2>>, compareArray> pq;
    int d[MAX_N];

    for (int & i : d) {
        i = MAX_DIST;
    }

    pq.push({0, 1});
    d[1] = 0;

    while (!pq.empty()) {
        array<int, 2> cur = pq.top(); pq.pop();
        if (d[cur[1]] != cur[0]) continue;

        for (array<int, 2> nxt : v[cur[1]]) {
            if (d[nxt[1]] <= d[cur[1]] + nxt[0]) continue;
            d[nxt[1]] = d[cur[1]] + nxt[0];
            pq.push({d[nxt[1]], nxt[1]});
        }
    }

    cout << d[N];

    return 0;
}