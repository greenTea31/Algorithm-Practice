#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int dp[50001];
    dp[0] = 0; dp[1] = 1;

    for (int i = 2; i <= n ; i++) {
        dp[i] = 50001;

        for (int j = 1; j*j <= i; j++) {
            dp[i] = min(dp[i], dp[i - j*j] + 1);
        }
    }

    cout << dp[n];
    return 0;
}