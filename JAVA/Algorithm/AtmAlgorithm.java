//백준 11399번 : ATM
// https://www.acmicpc.net/problem/11399

import java.util.Scanner;
public class AtmAlgorithm{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// 주어진 값 확인
		// 횟수
		int num = sc.nextInt();

		// 각 기다리는 값
		int[] input = new int [num];
		for(int k = 0; k < num; k++){
			input[k] = sc.nextInt();
		}

		// 버블 정렬을 통해 최솟값이 되도록 정렬
		for(int i = input.length - 1; i > 0; i--) {
			for(int j = 0; j < i; j++) {
				if(input[j] > input[j + 1]) {
					int temp = input[j];
					input[j] = input[j + 1];
					input[j + 1] = temp;
				}
			}
		}
		
		// 기다리는 시간 합 저장 변수 선언
		int sum = 0;

		// 부분합으로 전체 시간 합 구ㅁ
		for(int t = 0; t < input.length; t++)
		{	
			if ( t == 0){
				sum = sum + input[0];
			}
			if( t != 0){
			for(int m = 0; m <= t; m++){
				sum = sum + input[m];
			}
		}
		}
		
		// 결과 출력
		System.out.println(sum);

		sc.close();

	}
}