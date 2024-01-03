#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int solves[1001];

    for (int i = 0; i < N; i++) {
        cin >> solves[i];
    }

    int ans = 0;
    int strick = 0;

    for (int i = 0; i < N; i++) {
        if (solves[i] > 0) strick++;
        else strick = 0;
        ans = ans < strick ? strick : ans;
    }

    cout << ans;

    return 0;
}