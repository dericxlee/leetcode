/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let index = new Map();

    for(let i = 0; i < nums.length; i++){
        if(index.has(nums[i])) return [index.get(nums[i]), i]
        index.set(target - nums[i], i);
    };

    return false;
};