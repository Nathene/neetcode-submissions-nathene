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
    vector<int> rightSideView(TreeNode* root) {
        std::vector<int> result{};
        if (!root) return result;
        std::deque<TreeNode*> q{root};
        while (q.size() > 0) {
            int last{};
            int level = q.size();
            for (size_t i{}; i < level; ++i) {
                TreeNode* node = q.front();
                last = node->val;
                if (node->left) q.push_back(node->left);
                if (node->right) q.push_back(node->right);
                q.pop_front();
            }
            result.push_back(last);
        }
        return result;
    }
};
