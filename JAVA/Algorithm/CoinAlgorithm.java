//백준 11047번 : 동전 0
// https://www.acmicpc.net/problem/11047

import java.util.Scanner;
public class CoinAlgorithm {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// n과 k 값 받기
        int n = sc.nextInt();
        int k = sc.nextInt();

        // 동전 종류 담을 배열 선언
        int[] coinArray = new int[n];

        // 동전 종류 입력
        for(int i = 0; i < n; i++){
            coinArray[i] = sc.nextInt();
        }

        // 중간 변수 선언
        int temp = 0;

        for(int j = n-1; j >= 0; j--){
            if(k >= coinArray[j]){
                temp = temp + (int)Math.floor(k/coinArray[j]);
                k = k - (int)Math.floor(k/coinArray[j]) * coinArray[j]; 
        }
        if(k == 0){
            break;
        }
        }

        System.out.println(temp);
		sc.close();

	}
}
