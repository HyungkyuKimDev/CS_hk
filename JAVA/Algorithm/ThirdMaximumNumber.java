class Solution {
    public int thirdMax(int[] nums) {
        // 배열 원소의 수가 1인 경우와 2인 경우 조건식
        if(nums.length == 1){
            return nums[0];
        }else if(nums.length == 2){
            if(nums[0] <= nums[1]){
                return nums[1];
            }else if(nums[0] >= nums[1]){
                return nums[0];
            }
        }
        
        // 버블 정렬을 통해 값 정렬
        for(int i = 0; i < nums.length-1; i++) {
			for(int j = 0; j < nums.length-1-i; j++) { 
				if(nums[j] > nums[j+1]) {
					int tmp = nums[j]; 
					nums[j] = nums[j+1]; 
					nums[j+1] = tmp; 
				}
			}
		}

        // 중간값 저장할 변수, 값 크기 순서 저장할 변수
        int temp = nums[nums.length - 1];
        int val = 1;

        // 값이 더 적어질 경우, 값 크기 순서 늘리고 중간값 변경
        for(int k = nums.length-1; k >= 0; k--){
            if(nums[k] < temp){
                val++;
                temp = nums[k];
            }
            if(val == 3){
                return nums[k];
            }
        }
        return nums[nums.length-1];
    }
}