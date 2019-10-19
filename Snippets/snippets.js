// file of helper functions, code that I reuse often or foresee reusing often

// helper function that returns an object { value: count }
// when given an iterable
// JavaScript implementation of Python's Counter
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