#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    unordered_map<string, string> um;

    for (int i = 0; i < N; i++) {
        string address, password;
        cin >> address >> password;
        um[address] = password;
    }

    for (int i = 0; i < M; i++) {
        string address;
        cin >> address;
        cout << um[address] << '\n';
    }

    return 0;
}