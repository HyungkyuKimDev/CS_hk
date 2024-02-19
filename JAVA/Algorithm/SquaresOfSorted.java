// leetcode : Squares of a Sorted Array
// https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/

import java.util.Arrays;

class Solution {
    public int[] sortedSquares(int[] nums) {

        // 각각의 원소를 제곱함(제곱하면 마이너스인 요소도 자동 해결)
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != 0){
                nums[i] = nums[i] * nums[i];
            }
        }

        // 원소 정렬
        Arrays.sort(nums);

        // 결과 반환
        return nums;
    }
}