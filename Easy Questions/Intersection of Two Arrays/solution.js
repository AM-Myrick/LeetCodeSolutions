// https://leetcode.com/problems/intersection-of-two-arrays/
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    const set1 = new Set(nums1);
    const set2 = new Set(nums2);
    const result = [];
    
    for (let number of set1) {
        if (set2.has(number)) {
            result.push(number);
        }
    }
    return result;
};