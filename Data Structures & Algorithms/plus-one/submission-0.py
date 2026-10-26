class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i,num in enumerate(digits[::-1]):
            if num < 9:
                digits[-1 -i] += 1
                return digits
            else:
                digits[-1 - i] = 0
        


        return [1] + digits 
