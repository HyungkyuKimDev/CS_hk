// https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3574/
// leetcode : Squares of a Sorted Array

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {

        List<Integer> list = new ArrayList<Integer>();
        Arrays.sort(nums);        
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != i+1){
                if(Arrays.binarySearch(nums, i+1) <0){
                    list.add(i+1);
                }
            }
        }
        return list;
        }
    }