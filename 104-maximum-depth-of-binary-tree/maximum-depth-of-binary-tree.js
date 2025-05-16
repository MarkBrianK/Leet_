/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    if (root === null ){
        return 0
    }
    let rightLength = maxDepth(root.right);
    let leftLength = maxDepth(root.left)

    return Math.max(leftLength, rightLength) + 1
    
};