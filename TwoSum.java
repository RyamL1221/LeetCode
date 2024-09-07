public class TwoSum {
    
}

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] solution = {-1, -1};
        outerloop:
        for(int i = 0; i < nums.length; i++) {
            for(int j = i + 1; j < nums.length; j++) {
                if(nums[i] + nums[j] == target) {
                    solution[0] = i;
                    solution[1] = j;
                    break outerloop;
                }
            }
        }
        return solution;
    }
}