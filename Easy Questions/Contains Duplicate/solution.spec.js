const helpers = require('./solution.js');

test("returns true", () => {
    const input = [1,2,3,1];
    const expected = true;

    const result = helpers.containsDuplicate(input);
    expect(result).toBe(expected);
})

test("returns false", () => {
    const input = [1,2,3,4];
    const expected = false;

    const result = helpers.containsDuplicate(input);
    expect(result).toBe(expected);
})

test("returns true", () => {
    const input = [1,1,1,3,3,4,3,2,4,2];
    const expected = true;

    const result = helpers.containsDuplicate(input);
    expect(result).toBe(expected);
})