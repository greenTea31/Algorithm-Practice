import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] students = new int[N];

        for (int i = 0; i < N; i++) {
            students[i] = br.readLine().length();
        }

        int[] nameLength = new int[21];
        long answer = 0;

        for (int i = 0; i < K+1; i++) {
            if (i >= N) continue;
            answer += nameLength[students[i]];
            nameLength[students[i]] += 1;
        }

        int left = 0;
        int right = Math.min(N-1, K);

        while (right+1 < N) {
            nameLength[students[left++]] -= 1;
            answer += nameLength[students[++right]];
            nameLength[students[right]] += 1;
        }

        System.out.println(answer);
    } // end of main
}// end of class
