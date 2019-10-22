// https://leetcode.com/problems/length-of-last-word/
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    if (s === "") {
        return 0;
    }
    // turns s into an array and removes empty elements
    const copy = s.split(" ").filter(item => item !== "");
    return copy == false ? 0 : copy[copy.length - 1].length;
};