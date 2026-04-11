impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut l: usize = 0;
        let mut r: usize = nums.len();

        while l < r {
            let m: usize = l + (r - l) / 2;

            if nums[m] == target { return m as i32 }

            if nums[m] < target {
                l = m + 1;
            } else {
                r = m;
            }
        }

        -1
    }
}
