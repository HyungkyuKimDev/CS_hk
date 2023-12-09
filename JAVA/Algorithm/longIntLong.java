//백준 25314번 : 코딩은 체육과목 입니다 
// https://www.acmicpc.net/problem/25314

import java.util.Scanner;
public class longIntLong{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// 주어진 값 확인
		int input = sc.nextInt();
		
		// 4의 배수 확인 
		int n_num = (input/4);
		
		// 4의 배수 값 만큼, "long " 출력
        for(int i = 0; i < n_num; i++)
        {
            System.out.print("long ");
        }

		// 마지막으로 "int" 출력해서 마무리
		System.out.print("int");
		sc.close();

	}
}

