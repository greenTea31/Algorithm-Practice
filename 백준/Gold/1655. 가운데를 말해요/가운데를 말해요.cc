#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    priority_queue<int> max_pq;
    priority_queue<int, vector<int>, greater<int>> min_pq;

    int maxSize = 0;
    int minSize = 0;
    int N, num;
    cin >> N;

    while(N--) { // 7
        cin >> num;
        if (maxSize == minSize) {
            if (minSize != 0 && min_pq.top() < num) {
                max_pq.push(min_pq.top());
                min_pq.pop();
                min_pq.push(num);
                maxSize++;
            } else {
                max_pq.push(num);
                maxSize++;
            }
        } else if (maxSize > minSize) {
            if (max_pq.top() > num) {
                min_pq.push(max_pq.top());
                max_pq.pop();
                max_pq.push(num);
                minSize++;
            } else {
                min_pq.push(num);
                minSize++;
            }
        }

        cout << max_pq.top() << '\n';
    }


    return 0;
}