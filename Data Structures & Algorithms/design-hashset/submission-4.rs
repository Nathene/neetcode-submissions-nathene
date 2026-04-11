struct Node {
    key: i32,
    next: Option<Box<Node>>,
}

struct MyHashSet {
    buckets: Vec<Option<Box<Node>>>,
    size: usize,
    capacity: usize,
}

impl MyHashSet {
    pub fn new() -> Self {
        let initial_capacity = 50;
        Self {
            buckets: (0..initial_capacity).map(|_| None).collect(),
            size: 0,
            capacity: initial_capacity,
        }
    }

    fn hash(&self, key: i32) -> usize {
        (key.abs() as usize) % self.capacity
    }

    pub fn add(&mut self, key: i32) {
        if self.contains(key) { return; }

        // load factor (size / capacity > 0.75)
        if self.size * 4 > self.capacity * 3 {
            self.resize();
        }

        let idx = self.hash(key);
        let new_node = Box::new(Node {
            key,
            next: self.buckets[idx].take(),
        });

        self.buckets[idx] = Some(new_node);
        self.size += 1;
    }

    pub fn remove(&mut self, key: i32) {
        let idx = self.hash(key);
        let mut current = &mut self.buckets[idx];

        loop {
            match current {
                Some(node) if node.key == key => {
                    let next_node = node.next.take();
                    *current = next_node;
                    self.size -= 1;
                    return; 
                },
                Some(node) => {
                    current = &mut node.next;
                },
                None => break,
            }
        }
    }
    


    pub fn contains(&self, key: i32) -> bool {
        let idx = self.hash(key);
        let mut current = &self.buckets[idx];

        while let Some(node) = current {
            if node.key == key { return true; }
            current = &node.next;
        }

        false
    }

    fn resize(&mut self) {
        let old_buckets = std::mem::replace(&mut self.buckets, Vec::new());
        self.capacity *= 2;
        self.size = 0;
        self.buckets = (0..self.capacity).map(|_| None).collect();

        for mut node_opt in old_buckets {
            while let Some(mut node) = node_opt {
                node_opt = node.next.take();
                self.add(node.key);
            }
        }
    }
}

