impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();

        nums.iter()
            .enumerate()
            .find_map(|(i, &val)| {
                let remaining = target - val;
                if let Some(&prev_idx) = map.get(&remaining) {
                    Some(vec![prev_idx, i as i32])
                } else {
                    map.insert(val, i as i32);
                    None
                }
            })
            .unwrap_or_default()
    }
}
