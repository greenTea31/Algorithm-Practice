import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;


public class Main {
	// SN: SCC 개수, sn[i] = i가 속한 SCC의 번호
	static int[] visited;
	static boolean[] finished;
	static int cnt = 0;
	static ArrayDeque<Integer> s = new ArrayDeque<>();
	static ArrayList<ArrayList<Integer>> SCC;
	static ArrayList<Integer>[] al;
	static int SN = 0;
	static int[] sn;
	
	// 자신의 결과값을 리턴하는 DFS 함수
	static int dfs(int cur) {
		visited[cur] = ++cnt;
		s.addLast(cur);
		
		// 자신의 visited 번호, 자식들의 result나 visited중 가장 작은 번호를 result에 저장함
		int result = visited[cur];
		for (int nxt : al[cur]) {
			if (visited[nxt] == 0) result = Math.min(result, dfs(nxt));
			else if (!finished[nxt]) result = Math.min(result, visited[nxt]); 
		}
		
		// 자신, 자신의 자손들이 도달 가능한 제일 높은 정점이 자신일 경우 SCC 추출
		if (result == visited[cur]) {
			ArrayList<Integer> curScc = new ArrayList<>();
			
			while (true) {
				int t = s.pollLast();
				curScc.add(t);
				finished[t] = true;
				sn[t] = SN;
				if (t == cur) break;
			}
			
			Collections.sort(curScc);
			SCC.add(curScc);
			SN++;
		}
		
		return result;
	}
	
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	int V = Integer.parseInt(st.nextToken());
    	int E = Integer.parseInt(st.nextToken());
    	
    	al = new ArrayList[V+1];
    	visited = new int[V+1];
    	finished = new boolean[V+1];
    	sn = new int[V+1];
    	SCC = new ArrayList<>();
    	
    	for (int i = 0; i < V+1; i++) {
    		al[i] = new ArrayList<>();
    	}
    	
    	
    	for (int i = 0; i < E; i++) {
    		st = new StringTokenizer(br.readLine());
    		int A = Integer.parseInt(st.nextToken());
    		int B = Integer.parseInt(st.nextToken());
    		
    		al[A].add(B);
    	}
    	
    	for (int i = 1; i < V+1; i++) {
    		if (visited[i] == 0) dfs(i);
    	}
    	
    	System.out.println(SN);
    	
    	Collections.sort(SCC, (o1, o2) -> o1.get(0) - o2.get(0));
    	
    	for (ArrayList<Integer> SCCC : SCC) {
    		for (int num : SCCC) {
    			System.out.print(num + " ");
    		}
    		System.out.println(-1);
    	}
    }
}


