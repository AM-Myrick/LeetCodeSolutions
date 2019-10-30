// https://leetcode.com/problems/happy-number/
/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let copy = n.toString().split("");
    let total = 0;
    const seen = new Set();
    
    while (true) {
        for (let number of copy) {
            total += Math.pow(+number, 2);
        }
        if (total === 1) {
            return true;
        }
        if (seen.has(total)) {
            return false;
        }
        else {
            seen.add(total);
            copy = total.toString().split("");
            total = 0;
        }
    }
};