class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num
        res = []

        if zeros > 1:
            for num in nums:
                res.append(0)
            return res

        if zeros == 1:
            for num in nums:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            return res
        for num in nums:
            res.append(product // num)
        return res