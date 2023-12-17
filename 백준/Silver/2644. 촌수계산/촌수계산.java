import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer>[] al;
        int n = Integer.parseInt(br.readLine());
        al = new ArrayList[n+1];

        for (int i = 0; i <= n; i++) {
            al[i] = new ArrayList<Integer>();
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        
        int m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            al[start].add(end);
            al[end].add(start);
        }

        int answer = -1;
        
        ArrayDeque<int[]> q = new ArrayDeque<>();
        boolean[] visited = new boolean[n+1];
        visited[a] = true;
        q.add(new int[]{a, 0});
        boolean endFlag = false;

        while (!q.isEmpty()) {
            int[] cur = q.pollFirst();

            for (int nxt : al[cur[0]]) {
                if (visited[nxt]) continue;
                visited[nxt] = true;
                if (nxt == b) {
                    answer = cur[1]+1;
                    endFlag = true;
                    break;
                }
                q.add(new int[]{nxt, cur[1]+1});

            }

            if (endFlag) break;
        }

        System.out.println(answer);
    } // end of main
} // end of class
