#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool cut(long long mid, vector<long long>& vec, int N, int M) {
    long long sum = 0;

    for (int i = 0; i < N; i++) {
        if (vec[i] > mid) {
            sum += vec[i] - mid;
        }

        if (sum >= M) {
            return true;
        }
    }

    return false;
}

int main() {
    int N, M;
    cin >> N >> M;

    vector<long long> tree(N);

    for (int i = 0; i < tree.size(); i++) {
        cin >> tree[i];
    }

    long long left = 0;
    long long right = *max_element(tree.begin(), tree.end());
    long long mid;
    long long answer;

    while (left <= right) {
        mid = (left + right) / 2;
        if (cut(mid, tree, N, M)) {
            answer = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    cout << answer;

    return 0;
}