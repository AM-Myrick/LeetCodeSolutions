// https://leetcode.com/problems/palindrome-linked-list/
package main
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func isPalindrome(head *ListNode) bool {
    var copy []int
    for head != nil {
        copy = append(copy, head.Val)
        head = head.Next
    }
    // checks if each element matches the corresponding element
    // required for the linked list to be a palindrome
    for i, j := 0, len(copy) - 1; i < j; i, j = i + 1, j - 1 {
        if copy[i] != copy[j] {
            return false
        }
    }
    return true
}