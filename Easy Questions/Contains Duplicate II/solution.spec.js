const helpers = require('./solution.js');

test("returns true", () => {
    const input = [1,2,3,1];
    const k = 3;
    const expected = true;

    const result = helpers.containsNearbyDuplicate(input, k);
    expect(result).toBe(expected);
})

test("returns true", () => {
    const input = [1,0,1,1];
    const k = 1;
    const expected = true;

    const result = helpers.containsNearbyDuplicate(input, k);
    expect(result).toBe(expected);
})

test("returns false", () => {
    const input = [1,2,3,1,2,3];
    const k = 2;
    const expected = false;

    const result = helpers.containsNearbyDuplicate(input, k);
    expect(result).toBe(expected);
})