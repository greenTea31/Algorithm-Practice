import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int[] items = new int[n+1];
        int[][] edges = new int[n+1][n+1];
        st = new StringTokenizer(br.readLine());

        for (int i = 1; i <= n; i++) {
            items[i] = Integer.parseInt(st.nextToken());
        }
        
        int[][] d = new int[n+1][n+1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j) continue;
                d[i][j] = 1010101010;
            }
        }

        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            d[a][b] = l;
            d[b][a] = l;
        }

        for (int k = 1; k <= n; k++) {
            for (int i = 1 ; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (d[i][k] + d[k][j] >= d[i][j]) continue;
                    d[i][j] = d[i][k] + d[k][j];
                }
            }
        }

        int answer = 0;

        for (int i = 1; i <= n; i++) {
            int tempAnswer = 0;
            for (int j = 1; j <= n; j++) {
                if (d[i][j] <= m) tempAnswer += items[j];
            }
            answer = Math.max(answer, tempAnswer);
        }

        System.out.println(answer);
    } // end of main
}// end of class
