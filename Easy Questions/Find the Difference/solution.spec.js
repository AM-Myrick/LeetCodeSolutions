const helpers = require('./solution.js');

test("returns extra letter", () => {
    const inputOne = "abcd";
    const inputTwo = "abcde";
    const expected = "e";

    const result = helpers.findTheDifference(inputOne, inputTwo);
    expect(result).toBe(expected);
})