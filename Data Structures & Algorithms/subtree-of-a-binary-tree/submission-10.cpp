/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        
        auto is_same = [&](auto self, TreeNode* p, TreeNode* q) -> bool {
            if (p == nullptr && q == nullptr) return true;
            if (p == nullptr || q == nullptr || p->val != q->val) return false;

            return self(self, p->left, q->left) && self(self, p->right, q->right);
        };

        auto dfs = [&](auto self, TreeNode* node) -> bool {
            if (node == nullptr) return false;
            if (node->val == subRoot->val) {
                if (is_same(is_same, node, subRoot)) return true;
            }

            return self(self, node->left) || self(self, node->right);
        };

        return dfs(dfs, root);
    }
};
