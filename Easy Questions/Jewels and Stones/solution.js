// https://leetcode.com/problems/jewels-and-stones/
// You're given strings J representing the types of stones that are jewels, 
// and S representing the stones you have.  Each character in S is a type of stone you have.  
// You want to know how many of the stones you have are also jewels.

// The letters in J are guaranteed distinct, and all characters in J and S are letters. 
// Letters are case sensitive, so "a" is considered a different type of stone from "A".

// Example 1:
// Input: J = "aA", S = "aAAbbbb"
// Output: 3

// Example 2:
// Input: J = "z", S = "ZZ"
// Output: 0
// Note:

// S and J will consist of letters and have length at most 50.
// The characters in J are distinct.

/**
 * @param {string} J
 * @param {string} S
 * @return {number}
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

var numJewelsInStones = function(J, S) {
    // count the number of stones in S
    const stoneCounter = createCounter(S);
    let count = 0;
    
    // check which stones are jewels by iterating over J
    // and seeing if jewel is a property of stoneCounter
    for (let jewel of J) {
        if (stoneCounter[jewel]) {
            count += stoneCounter[jewel];
        }
    }
    
    return count;
};