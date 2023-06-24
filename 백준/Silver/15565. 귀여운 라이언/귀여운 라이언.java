import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] dolls = new int[N];
        int[] lions = new int[N];
        int lionAddIndex = 0;
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            dolls[i] = Integer.parseInt(st.nextToken());
            if (dolls[i] == 1) lions[lionAddIndex++] = i;
        }

        int left = 0;
        int right = K-1;
        int answer = Math.min(1000001, (lions[right] - lions[left] + 1));

        while (right + 1 < lionAddIndex) {
            left++; right++;
            answer = Math.min(answer , lions[right] - lions[left] + 1);
        }

        if (lionAddIndex < K) {
            System.out.println(-1);
        } else {
            System.out.print(answer);
        }
    } // end of main
}// end of class
