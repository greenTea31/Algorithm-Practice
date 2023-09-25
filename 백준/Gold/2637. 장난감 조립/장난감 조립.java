import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		int finalNode = 0;
		ArrayList<ArrayList<int[]>> al = new ArrayList<>();
		int[] inDegree = new int[N+1];
		
		for (int i = 0; i <= N; i++) {
			al.add(new ArrayList<>());
		}
		
		for (int i = 0; i < M; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int X = Integer.parseInt(st.nextToken());
			int Y = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			
			al.get(Y).add(new int[] {K, X});
			inDegree[X]++;
		}
		
		int basic = 0;
		ArrayDeque<Integer> q = new ArrayDeque<>();
		HashMap<Integer, Integer> coorCompression = new HashMap<>();
		HashMap<Integer, Integer> reverseCompression = new HashMap<>();
		
		for (int i = 1; i <= N; i++) {
			if (inDegree[i] == 0) {
				coorCompression.put(i, basic);
				reverseCompression.put(basic, i);
				basic++;
				q.addLast(i);
			}
		}
		
		int[][] needBasic = new int[N+1][basic];
		
		for (int i = 1; i <= N; i++) {
			if (inDegree[i] == 0) {
				needBasic[i][coorCompression.get(i)]++;
			}
		}
		
		while (!q.isEmpty()) {
			int cur = q.pollFirst();
			
			for (int[] next : al.get(cur)) {
				int nextNeed = next[0];
				int nextNode = next[1];
				inDegree[nextNode]--;
				
				for (int i = 0; i < basic; i++) {
					needBasic[nextNode][i] += nextNeed*(needBasic[cur][i]);
				}
				
				if (inDegree[nextNode] == 0) {
					q.addLast(nextNode);
					finalNode = nextNode;
				}
			}
		}
		
		for (int i = 0; i < basic; i++) {
			sb.append(reverseCompression.get(i)).append(' ').append(needBasic[finalNode][i]).append('\n');
		}
		
		System.out.print(sb.toString());
	}
}