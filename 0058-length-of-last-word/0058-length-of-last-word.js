/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let res = 0;
    for(let i=s.length-1; i>=0; i--) {
        if(s[i] != ' ') res++;
        else {
            if(res > 0) return res;
        }
    }
    return res;
};