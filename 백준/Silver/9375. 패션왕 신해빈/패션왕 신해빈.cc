#include <iostream>
#include <utility>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        int n;
        cin >> n;
        unordered_map<string, int> um;

        for (int i = 0; i < n; i++) {
            string clothe, type;
            cin >> clothe >> type;
            if (um.find(type) == um.end()) {
                um[type] = 1;
            } else {
                um[type]++;
            }
        }

        int ans = 1;

        for (const auto& key : um) {
            ans *= (key.second + 1);
        }

        ans -= 1;

        cout << ans << '\n';
    }

    return 0;
}