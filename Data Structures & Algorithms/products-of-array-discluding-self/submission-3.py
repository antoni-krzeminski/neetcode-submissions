class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive approach would be o(n^2) with just counting it for every number separately
        # but we can make it o(n) by counting all the product and after that dividing by nums[i]
        product = 1
        zeros = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zeros += 1
                if zeros > 1:
                    return [0] * len(nums)
        output = []
        
        for num in nums:
            if num == 0:
                output.append(product)
            else:
                if zeros == 1:
                    output.append(0)
                else:
                    output.append(product // num)
        return output
        


