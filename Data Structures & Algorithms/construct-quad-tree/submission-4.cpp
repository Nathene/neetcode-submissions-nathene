/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {
        return build(grid, 0, 0, grid.size());
    }

private:
    Node* build(vector<vector<int>>& grid, int r, int c, int n) {
        // Base case: single pixel is always a leaf
        if (n == 1) {
            return new Node(grid[r][c], true);
        }

        int half = n / 2;
        Node* tl = build(grid, r, c, half);
        Node* tr = build(grid, r, c + half, half);
        Node* bl = build(grid, r + half, c, half);
        Node* br = build(grid, r + half, c + half, half);

        // Check if all 4 children are leaves and have the same value
        if (tl->isLeaf && tr->isLeaf && bl->isLeaf && br->isLeaf &&
            tl->val == tr->val && tr->val == bl->val && bl->val == br->val) {
            
            bool value = tl->val;
            // Clean up memory of child nodes we no longer need
            delete tl; delete tr; delete bl; delete br;
            
            return new Node(value, true);
        }

        // If they aren't the same, this is an internal node
        return new Node(false, false, tl, tr, bl, br);
    }
};