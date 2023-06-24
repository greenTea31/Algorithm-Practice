import java.io.*;
import java.util.*;

public class Main {
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            int[] home = new int[N];
            st = new StringTokenizer(br.readLine());

            for (int i = 0; i < N; i++) {
                home[i] = Integer.parseInt(st.nextToken());
            }

            int stolenMoney = 0;
            int answer = 0;

            for (int i = 0; i < M; i++) {
                stolenMoney += home[i];
            }

            if (stolenMoney < K) answer++;

            if (N == M) {
                sb.append(answer).append('\n');
                continue;
            }

            int left = 0;
            int right = M-1;

            while (left + 1 < N) {
                stolenMoney -= home[left++];

                if (right + 1 == N) {
                    right = 0;
                } else {
                    right++;
                }

                stolenMoney += home[right];

                if (stolenMoney < K) answer++;
            }

            sb.append(answer).append('\n');
        }

        System.out.print(sb.toString());
    } // end of main
}// end of class
