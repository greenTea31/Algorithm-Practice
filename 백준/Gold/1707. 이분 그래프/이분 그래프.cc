#include <stdio.h>

int K, V, E;

typedef struct st
{
	int node;
	struct st *next;
}NODE;

NODE HEAD[20200];
NODE POOL[202000 * 2];
int pcnt;

int check[20200];

void init()
{
	pcnt = 0; /* 메모리 풀 초기화 */
    
	for (int i = 1; i <= V;i++) HEAD[i].next = 0, check[i] = 0;
}

void Make(int p, int c)
{
	NODE *nd = &POOL[pcnt++];

	nd->node = c;

	nd->next = HEAD[p].next;
	HEAD[p].next = nd;
}

int DFS(int node, int color)
{
	check[node] = color;

	for (NODE *p = HEAD[node].next; p; p = p->next)
	{
		if (check[p->node] == color) return 0;
		if (!check[p->node])
		{
        	/* 3 - 1 = 2 <-> 3 - 2 = 1 */
			if (!DFS(p->node, 3 - color)) return 0;
		}
	}

	return 1;
}

int main(void)
{
	scanf("%d", &K);

	for (int tc = 1; tc <= K;tc++)
	{
		int flag;
		scanf("%d %d", &V, &E);

		init();

		for (int i = 0; i < E;i++)
		{
			int p, c;

			scanf("%d %d", &p, &c);
			Make(p, c);
			Make(c, p);
		}

		flag = 0;
		for (int i = 1; i <= V;i++)
		{
			if (!check[i])
			{
				flag = DFS(i, 1);
				if (!flag) break;
			}
		}

		if (flag) printf("YES\n");
		else printf("NO\n");
	}

	return 0;
}