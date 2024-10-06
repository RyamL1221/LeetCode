public class TwoSum {
    
}

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        int[] solution = new int[2];
        for(int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if(hashMap.containsKey(diff)) {
                return new int[] {hashMap.get(diff), i};
            } else {
                hashMap.put(nums[i], i);
            }
        }
        return new int[] {};
    }
}
