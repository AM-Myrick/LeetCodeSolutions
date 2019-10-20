const helpers = require('./solution.js');

test("returns extra letter", () => {
    const input = 15
    const expected = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ];

    const result = helpers.fizzBuzz(input);
    expect(result).toStrictEqual(expected);
})