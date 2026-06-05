package runningsumof1darray

//nums := [1,2,3,4]

func runningSumB(nums []int) []int {

	for i := 0; i < len(nums); i++ {
		nums[i] = nums[i - 1] + nums[i]
	}
	return nums
}