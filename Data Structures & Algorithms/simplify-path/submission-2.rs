impl Solution {
    pub fn simplify_path(path: String) -> String {
        let mut stack: Vec<&str> = Vec::new();

        for component in path.split('/') {
            match component {
                "." | "" => continue,
                ".." => {
                    stack.pop();
                }
                _ => {
                    stack.push(component);
                }
            }
        }
        String::from("/") + &stack.join("/") 
    }
}
