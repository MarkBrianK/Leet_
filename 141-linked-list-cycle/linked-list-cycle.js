/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    a = head
    b = head

    while( a !==null&& b!==null && b.next !== null){
        a = a.next
        b = b.next.next

        if (a===b){
            return true
        }
    }

    return false
    
};