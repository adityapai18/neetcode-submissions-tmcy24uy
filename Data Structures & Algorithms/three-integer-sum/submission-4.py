class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):

            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            l = i+1
            r = len(nums) - 1

            while l < r:
                tsum = num + nums[l] + nums[r]

                if tsum > 0:
                    r-=1
                elif tsum<0:
                    l+=1
                
                if tsum == 0:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l <r:
                        l+=1
        return res
        