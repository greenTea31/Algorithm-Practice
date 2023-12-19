#include <iostream>
#include <algorithm>
using namespace std;

int main()  {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int K;
    cin >> K;

    for (int i = 1; i <= K; ++i) {
        int N;
        cin >> N;
        int* scores = new int[N];

        for (int j = 0; j < N; ++j) {
            cin >> scores[j];
        }

        sort(scores, scores + N, greater<>());

        int maxScore = scores[0];
        int minScore = scores[N-1];
        int maxDiff = 0;

        for (int j = 0; j < N-1; ++j) {
            int diff = scores[j] - scores[j+1];
            maxDiff = diff > maxDiff ? diff : maxDiff;
        }

        cout << "Class " << i << '\n';
        cout << "Max " << maxScore << ", Min " << minScore << ", Largest gap " << maxDiff << '\n';
        delete[] scores;
    }
}