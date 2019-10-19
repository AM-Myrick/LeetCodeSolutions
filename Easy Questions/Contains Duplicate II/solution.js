// https://leetcode.com/problems/contains-duplicate-ii/
// Given an array of integers and an integer k, find out whether there are two distinct indices 
// i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

// Example 1:
// Input: nums = [1,2,3,1], k = 3
// Output: true

// Example 2:
// Input: nums = [1,0,1,1], k = 1
// Output: true

// Example 3:
// Input: nums = [1,2,3,1,2,3], k = 2
// Output: false

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    // create an object and add all numbers in nums to it by { index: value }
    // if the number is already in nums, check if the absolute difference
    // between current index and last saved index is <= k
    // if the loop finishes, return false
    const copy = {};
    for (let index in nums) {
        const number = nums[index];
        if (copy[number]) {
            const originalIndex = copy[number];
            if (Math.abs(index - originalIndex) <= k) {
                return true
            }
        }
        copy[number] = index;
    }
    return false;
};

module.exports = {
    containsNearbyDuplicate
}