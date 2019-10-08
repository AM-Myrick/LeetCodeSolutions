// https://leetcode.com/problems/sqrtx/submissions/
package main
import "math"
func mySqrt(x int) int {
    // math.Pow only accepts valid float64 types
    return int(math.Pow(float64(x), 0.5))
}