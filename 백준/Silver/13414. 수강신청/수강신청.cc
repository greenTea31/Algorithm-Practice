#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int K, L;
    cin >> K >> L;

    unordered_map<string, int> s;
    vector<string> v;

    for (int i = 0; i < L; i++) {
        string input;
        cin >> input;

        if (s.find(input) == s.end()) {
            s[input] = 0;
        } else {
            s[input]++;
        }

        v.push_back(input);
    }

    int size = v.size();
    int index = -1;
    int output = 0;

    while (size-- && output < K) {
        index++;

        if (s[v[index]] > 0) {
            s[v[index]]--;
            continue;
        } else {
            cout << v[index] << '\n';
            output++;
        }
    }

    return 0;
}