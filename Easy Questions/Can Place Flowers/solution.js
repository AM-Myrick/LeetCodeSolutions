// https://leetcode.com/problems/can-place-flowers/
// TODO - refactor
/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    if (n === 0 || flowerbed[0] === 0 && flowerbed.length === 1) {
        return true;
    }
    if (flowerbed[0] === 0 && flowerbed[1] === 0) {
        flowerbed[0] = 1;
        n--;
    }
    if (flowerbed[flowerbed.length - 1] === 0 && flowerbed[flowerbed.length - 2] === 0) {
        flowerbed[flowerbed.length - 1] = 1;
        n--;
    }
    if (n <= 0) {
        return true;
    }
    for (let i = 1; i <= flowerbed.length; i++) {
        if (flowerbed[i - 1] === 0 && flowerbed[i] === 0 && flowerbed[i + 1] === 0) {
            flowerbed[i] = 1;
            n--;
            if (n === 0) {
                return true;
            }
        }
    }
    return false;
};