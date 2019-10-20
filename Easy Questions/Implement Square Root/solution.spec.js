const helpers = require('./solution.js');

test("returns square root", () => {
    const input = 4
    const expected = 2;

    const result = helpers.mySqrt(input);
    expect(result).toStrictEqual(expected);
})

test("returns square root", () => {
    const input = 8
    const expected = 2;

    const result = helpers.mySqrt(input);
    expect(result).toStrictEqual(expected);
})