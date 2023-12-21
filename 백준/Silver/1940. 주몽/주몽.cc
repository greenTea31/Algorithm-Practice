#include <iostream>
#include <algorithm>
#define MAX 15001
using namespace std;
int numbers[MAX];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; ++i) {
        cin >> numbers[i];
    }

    sort(numbers, numbers+N);

    int left = 0; int right = N-1;
    int ans = 0;

    while (left < right) {
        int sum = numbers[left] + numbers[right];

        if (sum == M) {
            left++;
            right--;
            ans++;
        }
        else if (sum < M) left++;
        else if (sum > M) right--;
    }

    cout << ans;

    return 0;
}