// https://leetcode.com/problems/find-the-difference/

// Given two strings s and t which consist of only lowercase letters.
// String t is generated by random shuffling string s and then add one more letter at a random position.
// Find the letter that was added in t.

// Example:
// Input:
// s = "abcd"
// t = "abcde"

// Output:
// e

// Explanation:
// 'e' is the letter that was added.

/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */

// helper function that returns an object { value: count }
// when given an iterable
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

var findTheDifference = function(s, t) {
    // create counters from parameters
    // iterate over the longer counter (t)
    // check if a letter in counter_t is not in counter_s
    // check if a letter appears more in counter_t than counter_s
    // in either situation, return the letter
    
    const counter_t = createCounter(t);
    const counter_s = createCounter(s);
    
    for (let letter in counter_t) {
        if (!counter_s[letter] || counter_t[letter] > counter_s[letter]) {
            return letter;
        }
    }
};

module.exports = {
    findTheDifference
}