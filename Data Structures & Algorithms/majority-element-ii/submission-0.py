class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        ans = []
        for key in counter:
            if counter[key] > len(nums) // 3:
                ans.append(key)
        return ans