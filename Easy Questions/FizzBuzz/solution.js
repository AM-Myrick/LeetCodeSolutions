// https://leetcode.com/problems/fizz-buzz/
// Write a program that outputs the string representation of numbers from 1 to n.

// But for multiples of three it should output “Fizz” instead of the number 
// and for the multiples of five output “Buzz”. 
// For numbers which are multiples of both three and five output “FizzBuzz”.

// Example:
// n = 15,

// Return:
// [
//     "1",
//     "2",
//     "Fizz",
//     "4",
//     "Buzz",
//     "Fizz",
//     "7",
//     "8",
//     "Fizz",
//     "Buzz",
//     "11",
//     "Fizz",
//     "13",
//     "14",
//     "FizzBuzz"
// ]

/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    const resultArray = []
    for (let i = 1; i <= n; i++) {
        let result = "";
        result += i % 3 === 0 ? "Fizz": "";
        result += i % 5 === 0 ? "Buzz": "";
        result = result === "" ? `${i}`: result;
        resultArray.push(result);
    }
    return resultArray;
};

module.exports = {
    fizzBuzz
}