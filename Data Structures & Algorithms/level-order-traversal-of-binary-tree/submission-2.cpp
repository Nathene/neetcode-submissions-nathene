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
    vector<vector<int>> levelOrder(TreeNode* root) {
        std::vector<std::vector<int>> result{};
        if (!root) return result;

        std::deque<TreeNode*> q{root};
        while (!q.empty()) {
            int level = q.size();
            std::vector<int> curr_level{};
            for (int i{}; i < level; ++i) {
                TreeNode* node = q.front();
                q.pop_front();
                curr_level.push_back(node->val);
                if (node->left) q.push_back(node->left);
                if (node->right) q.push_back(node->right);
            }
            result.push_back(std::move(curr_level));
        }
        return result;

    }
};
