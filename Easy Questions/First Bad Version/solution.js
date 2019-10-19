// https://leetcode.com/problems/first-bad-version/
// You are a product manager and currently leading a team to develop a new product. 
// Unfortunately, the latest version of your product fails the quality check. 
// Since each version is developed based on the previous version, 
// all the versions after a bad version are also bad.

// Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
// which causes all the following ones to be bad.

// You are given an API bool isBadVersion(version) which will return whether version is bad. 
// Implement a function to find the first bad version. 
// You should minimize the number of calls to the API.

// Example:
// Given n = 5, and version = 4 is the first bad version.

// call isBadVersion(3) -> false
// call isBadVersion(5) -> true
// call isBadVersion(4) -> true

// Then 4 is the first bad version. 

/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        if (n === 1) {
            return n;
        }
        // implement binary search to cut our iterations in half
        // starts with the lowest possible number and the highest (n)
        // calculate the middle and test if it's a bad version
        // if it is, the middle becomes the new high
        // this cuts out all indexes between middle and high
        // if it isn't, the middle + 1 becomes the new low
        // this cuts out all indexes between low and middle
        // the loop ends once low is greater than or equal to the high
        let low = 0;
        let high = n;
        
        while (low < high) {
            const middle = Math.floor((low + high) / 2);
            if (isBadVersion(middle)) {
                high = middle;
            }
            else {
                low = middle + 1;
            }
        }
        return low;
    };
};