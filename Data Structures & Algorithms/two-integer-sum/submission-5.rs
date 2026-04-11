impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut scores: HashMap<i32, i32> = HashMap::new();

        for (i, val) in nums.iter().enumerate() {
            let remaining = target - val;
            if let Some(ind) = scores.get(&remaining) {
                return vec![*ind, i as i32];
            }
            scores.insert(*val, i as i32);
        }

        vec![]
    }
}
