// https://leetcode.com/problems/student-attendance-record-i/
/**
 * @param {string} s
 * @return {boolean}
 */
var checkRecord = function(s) {
    if (s.includes("LLL")) {
        return false;
    }
    let absenceCount = 0;
    for (let letter of s) {
        if (letter === "A") {
            absenceCount++;
            if (absenceCount > 1) {
                return false;
            }
        }
    }
    return true;
};