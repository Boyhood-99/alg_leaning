class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return [] # 临界判断
        nums = sorted(nums, reverse=False)
        res = set()              # 去重                         
        for i, v in enumerate(nums[:-2]):
            if v > 0: break         # 剪枝优化
            start, end = i + 1, len(nums) - 1
            while start < end:
                if v + nums[start] + nums[end] > 0:
                    end -= 1
                elif v + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    temp = (v, nums[start], nums[end])
                    # temp = sorted(temp, reverse=False)  # 排序去除重复
                    res.add((temp[0], temp[1], temp[2]))
                    start += 1
        return list(res)

nums = [-1,0,0,1,2,-1,-4]

sol = Solution()
# print(sol.threeSum(nums))

res = []

sub_res = [[1,2],[2,3]]
for j in range(len(sub_res)): res.append([-1] + sub_res[j])
         
print(res)