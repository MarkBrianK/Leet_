/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    for (char of nums){
        if(char === target){
            let index = nums.indexOf(char)
            return index
        } 
    }
    return -1
};