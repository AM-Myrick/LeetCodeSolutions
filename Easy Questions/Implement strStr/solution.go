// https://leetcode.com/problems/implement-strstr/
package main
import "strings"
func strStr(haystack string, needle string) int {
    if needle == "" {
        return 0
    }
    return strings.Index(haystack, needle)
}