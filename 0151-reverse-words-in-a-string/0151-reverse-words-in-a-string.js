/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    queue = [];
    const array = s.split(' ');

    for (let i = 0; i < array.length; i++ ){
        if(array[i].length){
            queue.unshift(array[i]); 
        };
    };

    return queue.join(' ')
};