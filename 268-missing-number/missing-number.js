/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    const n = nums.length
    const range = Array.from({length: n+1}, (_,x)=> x)
    const missing = range.filter(num => !nums.includes(num))

    return missing[0]

    
    
};