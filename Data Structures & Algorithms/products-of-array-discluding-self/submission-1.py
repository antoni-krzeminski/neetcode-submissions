class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = []
        for i in range(len(nums)):
            mul = 1
            L1 = nums[:i]
            L2 = nums[i+1:]
            print(L1)
            print(L2)
            print("----")
            for x in L1:
                mul = mul * x
            for y in L2:
                mul = mul * y
            L.append(mul)
        return L


