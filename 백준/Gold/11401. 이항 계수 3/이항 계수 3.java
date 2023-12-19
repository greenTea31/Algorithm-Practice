import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static StringBuilder sb = new StringBuilder();
	
	// a^b의 값을 구해주는 함수로 거듭제곱을 사용한다
	static long pow(long a, int b) {
		if (b == 0) return 1;
		else if (b == 1) return a;
		else {
			long answer = pow(a, b/2);
			answer %= 1234567891;
			
			if (b % 2 == 0) {
				return (answer * answer) % 1000000007;
			} else {
				return (((answer * answer) % 1000000007) * a) % 1000000007;
			}
		}
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long[] factorial = new long[4000001];
        
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	int N = Integer.parseInt(st.nextToken());
    	int K = Integer.parseInt(st.nextToken());
    	factorial[0] = 1; factorial[1] = 1;
    	
    	for (int i = 2; i <= 4000000; i++) {
    		factorial[i] = factorial[i-1] * i;
    		factorial[i] %= 1000000007;
    	}
    	
    	long answer = factorial[N];
    	long multiple = (factorial[N-K] * factorial[K]) % 1000000007;
    	multiple = pow(multiple, 1000000005);
    	answer *= multiple;
    	answer %= 1000000007;
    	System.out.println(answer);
        
        System.out.print(sb.toString());
    }
    
}