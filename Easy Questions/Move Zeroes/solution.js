/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let count = 0;
    let idx = 0;
    while (idx < nums.length) {
        if (nums[idx] === 0) {
            nums.splice(idx, 1);
            count++;
            continue;
        }
        idx++;
    }
    while (count > 0) {
        nums.push(0);
        count--;
    }
};