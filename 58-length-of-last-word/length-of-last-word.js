/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    return s.split(" ").filter(word => word.length > 0).pop().length;
    
};