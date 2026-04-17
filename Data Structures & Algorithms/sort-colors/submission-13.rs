impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut l = 0;

        for i in 0..nums.len() {
            if nums[i] == 0 {
                nums.swap(l, i);
                l += 1;
            }
        }

        for i in l..nums.len() {
            if nums[i] == 1 {
                nums.swap(l, i);
                l += 1
            }
        }
    }
}
