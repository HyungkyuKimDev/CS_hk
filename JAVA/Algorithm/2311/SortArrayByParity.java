// Sort Array By Parity
// https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/

// Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
// Return any array that satisfies this condition.

// Input: nums = [3,1,2,4]
// Output: [2,4,3,1]
// Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int[] james = new int[nums.length];
        int temp = 0;
        for(int i = 0; i < nums.length; i++){
            if (nums[i] % 2 == 0){
                james[temp] = nums[i];
                if(temp == nums.length - 1){
                    break;
                }
                temp++;
            }
        }
        for(int i = 0; i < nums.length; i++){
            if (nums[i] % 2 != 0){
                james[temp] = nums[i];
                temp++;
            }
        }
        return james;
    }
}