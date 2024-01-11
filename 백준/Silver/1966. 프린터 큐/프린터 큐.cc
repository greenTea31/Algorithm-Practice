#include <iostream>
#include <array>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T ; tc++) {
        queue<array<int, 2>> q;

        int N, M;
        cin >> N >> M;

        int max_important[101];

        for (int i = 0 ; i < N; i++) {
            int input;
            cin >> input;

            max_important[i] = input;
            q.push({input, i});
        }

        sort(max_important, max_important+N, [](int a, int b) {
            return a > b;
        });

        int output = 0;

        while (!q.empty()) {
            if (q.front()[0] == max_important[output]) {
                if (q.front()[1] == M) {
                    output++;
                    break;
                }

                q.pop();
                output++;
            } else {
                q.push(q.front());
                q.pop();
            }
        }

        cout << output << '\n';
    }

    return 0;
}