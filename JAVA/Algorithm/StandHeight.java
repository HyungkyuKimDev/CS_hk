// Leet Code : Height Checker
// https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/

class StandHeight {
    public int heightChecker(int[] heights) {
        // 새로운 배열 생성
        int[] newHeight = new int[heights.length];

        // 기존 배열을 복사
        for(int m = 0; m < heights.length; m++){
            newHeight[m] = heights[m];
        }

        // 새로운 배열을 버블 정렬함
        for(int i = 0; i < newHeight.length-1; i++) { 
			for(int j = 0; j < newHeight.length-1-i; j++) { 
				if(newHeight[j] > newHeight[j+1]) {
					int tmp = newHeight[j]; 
					newHeight[j] = newHeight[j+1]; 
					newHeight[j+1] = tmp; 
				}
			}
        }

        // 중간값 저장 변수 선언
        int k = 0;
        
        // 새로운 배열과 기존 배열이 다른 만큼 중간값 저장 변수 증가
        for(int m = 0; m < heights.length; m++){
            if(newHeight[m] != heights[m]){
                k++;
            }
        }

        // 중간값 저장 변수 반환
        return k;
    }
}