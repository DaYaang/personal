
class Solution(object):
    def twoSum(self, nums, target):
        sum_dict = {}
        for index,num in enumerate(nums):
            othernum = target - num
            if othernum in sum_dict:
                print(f"最终返回index{sum_dict[othernum]}，另一个index{index}")
                return sum_dict[othernum],index
            sum_dict[num] = index
            print(sum_dict)


s1 = Solution()
s1.twoSum([11,22,33,4,44],77)