// https://leetcode.com/problems/sort-array-by-parity/
/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function(A) {
    let evens = [];
    let idx = 0;
    
    while (idx < A.length) {
        if (A[idx] % 2 === 0) {
            evens.push(A.splice(idx, 1));
            continue;
        }
        idx++;
    }
    
    return evens.concat(A)
};