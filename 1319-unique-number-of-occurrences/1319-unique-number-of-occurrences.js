/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
      let counts = new Map();

    for(let i = 0; i < arr.length; i++){
        if(!counts.has(arr[i])) {
            counts.set(arr[i], 1);
        } else {
            const count = counts.get(arr[i]);
            counts.set(arr[i], count + 1);
        };
    };


    const values = Array.from(counts.values());
    const set = new Set(values);
    return set.size === values.length;

};