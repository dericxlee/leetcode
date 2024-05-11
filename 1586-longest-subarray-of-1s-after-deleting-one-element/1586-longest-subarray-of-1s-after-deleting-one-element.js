/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let max = 0, left = 0, right = 0, k = 1;

    while(right < nums.length){
        if(nums[right] === 0) k--
        if(k < 0){
            if(nums[left] === 0) k++
            left++
        }
        right++
    };

    return right - left - 1;
};