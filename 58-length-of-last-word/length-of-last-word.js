/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let arr = s.split(" ").filter(word => word.length > 0);
    const lastElement = arr.pop()
    let count = 0;

    for (let i = 0; i<lastElement.length; i++){
        count++
    }

    return count

    
};