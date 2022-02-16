class Solution:
	def threeSum(self, nums: List[int] ->List[List[int]:
		res = []
		l = len(nums)
		nums.sort()
		for i in range(l - 2):
			if i > 0 and nums[i] == nums[i - 1]
				continue
			left,right = i + 1, l - 1
			while left < right:
				cur_sum = nums[i] + nums[left] + nums[right]
				if cur_sum < 0:
					left += 1
				elif cur_sum > 0:
					right -= 1
				else:
					res.append((nums[1], nums[left], nums[right]))
					while left < right and nums[left] == nums[left + 1]:
						left += 1
						
					left += 1
	return res				