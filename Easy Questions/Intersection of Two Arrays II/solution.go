// Package arrayintersect2 description - https://leetcode.com/problems/intersection-of-two-arrays-ii/
package arrayintersect2

func intersect(nums1 []int, nums2 []int) []int {
	numsMap := make(map[int]int)
	result := make([]int, 0, len(nums1))

	for _, num := range nums1 {
		if _, ok := numsMap[num]; ok {
			numsMap[num]++
			continue
		}
		numsMap[num] = 1
	}

	for _, num := range nums2 {
		if val, ok := numsMap[num]; ok {
			if val > 0 {
				result = append(result, num)
				numsMap[num]--
			}
		}
	}
	return result
}
