class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        for n in nums:
            mul = mul * n
        L = []

        if nums.count(0) > 1:
            for _ in nums:
                L.append(0)
        if nums.count(0) == 1:
            mul = 1
            for x in nums:
                if x != 0:
                    mul = mul * x
            for y in nums:
                if y == 0:
                    L.append(mul)
                else:
                    L.append(0)
        if nums.count(0) == 0:
            for n in nums:

                L.append(mul // n)

        return L


