// https://leetcode.com/problems/contains-duplicate/
// Given an array of integers, find if the array contains any duplicates.
// Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

// Example 1:
// Input: [1,2,3,1]
// Output: true

// Example 2:
// Input: [1,2,3,4]
// Output: false

// Example 3:
// Input: [1,1,1,3,3,4,3,2,4,2]
// Output: true
/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = (nums) => {
    // create a set and push all numbers in nums to it
    // if the number is already in nums, return true
    // if the loop finishes, return false
    const copy = new Set();
    for (let num of nums) {
        if (copy.has(num)) {
            return true;
        }
        copy.add(num);
    }
    return false;
};