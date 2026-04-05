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
    TreeNode* insertIntoBST(TreeNode* root, int val) {

        if (root == nullptr) return new TreeNode(val);
        
        TreeNode* curr = root;
        auto insert = [&](auto self) -> void {
            if (curr == nullptr) return;

            if (curr->val < val) {
                if (curr->right == nullptr) {
                    curr->right = new TreeNode(val);
                    return;
                }
                curr = curr->right;
                self(self);
            } else {
                if (curr->val > val) {
                    if (curr->left == nullptr) {
                        curr->left = new TreeNode(val);
                        return;
                    }
                    curr = curr->left;
                    self(self);
                }
            }
        };
        insert(insert);
        return root;

        }
};