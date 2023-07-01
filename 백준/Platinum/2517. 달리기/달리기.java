import java.io.*;
import java.util.*;

public class Main {
    static int[] segmentTree;
    static int nodeCount;
    static StringBuilder sb = new StringBuilder();

    static int getLowScoreCount(int L, int R, int nodeIndex, int nodeL, int nodeR) {
        if (nodeR < L || R < nodeL) return 0;
        if (L <= nodeL && nodeR <= R) return segmentTree[nodeIndex];
        int mid = (nodeL + nodeR) / 2;
        return getLowScoreCount(L, R, nodeIndex*2, nodeL, mid)
        + getLowScoreCount(L, R, nodeIndex*2+1, mid+1, nodeR);
    }

    static void update(int i) {
        int leafPlus = nodeCount/2 - 1;
        i += leafPlus;
        segmentTree[i] += 1;
        while (i > 1) {
            i >>= 1;
            segmentTree[i] += 1;
        }
    }

    public static void main(String[] args) throws IOException {
        // 선수의 수 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // 각 선수의 달리기 실력 저장
        int[] score = new int[N];
        int[] temp_score = new int[N];

        for (int i = 0; i < N; i++) {
            score[i] = Integer.parseInt(br.readLine());
            temp_score[i] = score[i];
        }

        // 실력을 50만 이하로 압축
        Arrays.sort(temp_score);
        HashMap<Integer, Integer> hm = new HashMap<>();

        for (int i = 0; i < N; i++) {
            hm.put(temp_score[i], i+1);
        }

        for (int i = 0; i < N; i++) {
            score[i] = hm.get(score[i]);
        }

        // N개의 리프 노드를 갖는 세그먼트 트리 선언
        nodeCount = 1;

        while (nodeCount < 2*N) {
            nodeCount <<= 1;
        }

        segmentTree = new int[nodeCount];

        // 앞에서 부터 선수를 읽고 i 실력을 가진 선수를 세그먼트 트리의 i번째 리프노드에 저장 O(logN)
        // 새로운 선수의 실력을 읽고 자신보다 낮은 실력을 가진 선수들의 수를 세그먼트 트리에서 구함 O(logN)
        // 구한 후 현재 등수 - 낮은 실력 선수 수를 반환

        sb.append(1).append('\n');
        update(score[0]);

        for (int i = 1; i < N; i++) {
            int slowMan = getLowScoreCount(1, score[i]-1, 1, 1, nodeCount / 2);
            sb.append(i+1 - slowMan).append('\n');
            update(score[i]);
        }

        System.out.print(sb.toString());
    } // end of main
}// end of class
