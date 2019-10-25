// https://leetcode.com/problems/ransom-note/
/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */

const createCounter = (iterable) => {
    if (iterable == null) {
        return "createCounter only accepts an iterable";
    }
    const counter = {};
    for (let element of iterable) {
        if (counter[element]) {
            counter[element]++;
            continue;
        }
        counter[element] = 1;
    }
    return counter;
}

var canConstruct = function(ransomNote, magazine) {
    const noteCounter = createCounter(ransomNote);
    const magazineCounter = createCounter(magazine);
    
    for (let letter in noteCounter) {
        if (!magazineCounter[letter]) {
            return false;
        }
        if (magazineCounter[letter] - noteCounter[letter] < 0) {
            return false;
        }
    }
    return true;
};