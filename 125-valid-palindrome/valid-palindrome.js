/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    newString = s.toLowerCase().replace(/[^a-z0-9]/g, '')

    let reversed = newString.split('').reverse().join('');

    if (reversed === newString){
        return true
    }else{
        return false
    }

    
};