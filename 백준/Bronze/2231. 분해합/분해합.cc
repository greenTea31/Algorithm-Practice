#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    
    int ans = 0;

    for (int i = 0; i < N; i++) {
        int temp = i;
        int tempAns = i;

        while (temp > 0) {
            tempAns += (temp % 10);
            temp /= 10;
        }

        if (tempAns == N) {
            ans = i;
            break;
        }
    }

    cout << ans;

    return 0;
}