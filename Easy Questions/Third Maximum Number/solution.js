// https://leetcode.com/problems/third-maximum-number/
/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    let numsCopy = [...new Set(nums)];
    if (numsCopy.length < 3) {
        return Math.max(...numsCopy)
    }
    numsCopy.sort((a, b) => a - b);
    return numsCopy[numsCopy.length - 3]
};