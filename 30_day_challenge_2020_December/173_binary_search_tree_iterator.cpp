/****************************************************************
* Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
* Date created      : 20201209
* Problem link      : https://leetcode.com/problems/binary-search-tree-iterator/
****************************************************************/

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

class BSTIterator {
private:
    stack<TreeNode*> st;
public:
    BSTIterator(TreeNode *root) {
        find_left(root);
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        if (st.empty())
            return false;
        return true;
    }

    /** @return the next smallest number */
    int next() {
        TreeNode* top = st.top();
        st.pop();
        if (top->right != NULL)
            find_left(top->right);
            
        return top->val;
    }
    
    /** put all the left child() of root */
    void find_left(TreeNode* root)
    {
        TreeNode* p = root;
        while (p != NULL)
        {
            st.push(p);
            p = p->left;
        }
    }
};

// link: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
// Morris Traversal, inorder search without stack or recursion
// class BSTIterator {
// public:
// BSTIterator(TreeNode *root) {
//     p = root;
// }

// /** @return whether we have a next smallest number */
// bool hasNext() {
//     return p != NULL;
// }

// /** @return the next smallest number */
// int next() {
//     TreeNode *tmp;
//     int ret;
//     while(p) {
//         if (p->left == NULL) {  
//             ret = p->val;
//             p = p->right;
//             break;
//         }  
//         else {  
//             tmp = p->left;  
//             while (tmp->right != NULL && tmp->right != p)  
//                 tmp = tmp->right;  
//             if (tmp->right == NULL) {  
//                 tmp->right = p;  
//                 p = p->left;  
//             }  
//             else {
//                 ret = p->val;
//                 tmp->right = NULL;  
//                 p = p->right;
//                 break;
//             }  
//         }  
//     }
    
//     return ret;
// }

// TreeNode *p;
// };


/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */