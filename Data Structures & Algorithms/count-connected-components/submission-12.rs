struct UnionFind {
    parent: Vec<usize>,
    rank: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self {
            parent: (0..n).collect(),
            rank: vec![0; n],
        }
    }

    fn find(&mut self, mut p: usize) -> usize {
        while self.parent[p] != p {
            self.parent[p] = self.parent[self.parent[p]]; // Path compression - inverse ackermann
            p = self.parent[p];
        }
        self.parent[p]
    }

    fn union(&mut self, p: usize, q: usize) -> bool {
        let n1 = self.find(p);
        let n2 = self.find(q);

        if n1 == n2 {
            return false;
        }

        // find the rank.
        if self.rank[n1] > self.rank[n2] {
            self.parent[n2] = n1;
            self.rank[n1] += self.rank[n2];
        } else if self.rank[n2] > self.rank[n1] {
            self.parent[n1] = n2;
            self.rank[n2] += self.rank[n1];
        } else {
            self.parent[n2] = n1;
            self.rank[n1] += 1;
        }
        true
    }
}

impl Solution {
    pub fn count_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let mut uf = UnionFind::new(n as usize);
        let mut count = n;

        for edge in edges {
            let node1 = edge[0] as usize;
            let node2 = edge[1] as usize;
            if uf.union(node1, node2) {
                count -= 1
            }
        }
        count
    }
}
