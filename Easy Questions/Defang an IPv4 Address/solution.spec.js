const helpers = require('./solution.js');

test("returns defanged ipv4", () => {
    const input = "1.1.1.1";
    const expected = "1[.]1[.]1[.]1";

    const result = helpers.defangIPaddr(input);
    expect(result).toBe(expected);
})

test("returns defanged ipv4", () => {
    const input = "255.100.50.0";
    const expected = "255[.]100[.]50[.]0";

    const result = helpers.defangIPaddr(input);
    expect(result).toBe(expected);
})