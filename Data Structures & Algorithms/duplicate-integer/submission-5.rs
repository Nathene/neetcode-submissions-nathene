impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut map = HashSet::with_capacity(nums.len());

        nums.iter().any(|&x| !map.insert(x))
    }
}
