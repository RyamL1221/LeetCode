class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> chck = new HashMap<>();
        for (int x = 0; x < nums.length; x++) {
            if (chck.containsKey(target-nums[x])) {
                return new int[] {chck.get(target-nums[x]), x};
            }
            chck.put(nums[x],x);
        }
        return new int[]{-1};
    }
}