#include <iostream>
using namespace std;

struct NODE {
    int node;
    NODE* next;
};

NODE HEAD[20005];
NODE POOL[400010];

int pcnt;
int check[20005];

void make(int p, int c) { // p와 c를 연결함
    NODE* nd = &POOL[pcnt++];
    nd->node = c;
    nd->next = HEAD[p].next;
    HEAD[p].next = nd;
}

int DFS(int node, int color) {
    check[node] = color;

    for (NODE* p = HEAD[node].next; p ; p = p->next) {
        if (check[p->node] == color) return 0;

        if (!check[p->node]) {
            if (!DFS(p->node, 3 - color)) return 0;
        }
    }

    return 1;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int K, V, E;

    cin >> K;

    for (int tc = 0; tc < K; tc++) {
        pcnt = 0;
        cin >> V >> E;

        for (int i = 1; i <= V; i++) {
            check[i] = 0;
            HEAD[i].next = nullptr;
        }

        for (int i = 0; i < E; i++) {
            int p, c;
            cin >> p >> c;
            make(p, c);
            make(c, p);
        }

        bool isBipartite = true;

        for (int i = 1; i <= V; i++) {
            if (!check[i]) {
                isBipartite = DFS(i, 1);
                if (!isBipartite) break;
            }
        }

        if (isBipartite) cout << "YES\n";
        else cout << "NO\n";
    }

    return 0;
}
