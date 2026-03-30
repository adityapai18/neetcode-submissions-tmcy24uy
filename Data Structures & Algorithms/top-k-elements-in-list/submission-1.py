class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        index = {}
        for num in nums:
            index[num] = 1 + index.get(num, 0)

        arr = []

        for num, cnt in index.items():
            arr.append([cnt,num])
        
        arr.sort()
        
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

            

        