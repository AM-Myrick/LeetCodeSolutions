// https://leetcode.com/problems/remove-duplicates-from-sorted-array/
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let i = 0;
    let j = 1;
    while (i < nums.length - 1) {
        if (nums[i] === nums[j]) {
            nums.splice(i, 1);
            continue;
        }
        i++, j++;
    }
    return j;
};