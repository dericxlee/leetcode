/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    const max = Math.max(...candies)
    const new_arr = [];

    for (let i = 0; i < candies.length; i++){
        if(candies[i] + extraCandies >= max){
            new_arr.push(true);
        } else {
            new_arr.push(false);
        };
    };
    return new_arr;
};