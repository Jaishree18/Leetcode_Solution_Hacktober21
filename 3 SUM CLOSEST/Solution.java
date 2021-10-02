class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int diff =  Integer.MAX_VALUE;
        int ans = 0;
        if(nums.length < 3) return ans;
        for(int first = 0; first < nums.length; first++) {
            int head = first + 1;
            int tail = nums.length - 1;
            while(head < tail) {
                int sum3 = nums[head] + nums[tail] + nums[first];
                int d = Math.abs(sum3 - target);
                if(d == 0) return target;
                if(d < diff) {
                    diff = d;
                    ans = sum3;
                }
                if(sum3 > target) tail--;
                if(sum3 < target) head++;
            }
            // skip the same elements
            while(first < nums.length-1 && nums[first+1] == nums[first])
                first++;
        }
        return ans;
    }
}
