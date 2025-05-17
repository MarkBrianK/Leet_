/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    n = nums.length
    const count ={}

    for(char of nums){
        count[char] = (count[char] || 0) + 1
        if(count[char] > n/2){
            return char
    }
    }
    return

    
};