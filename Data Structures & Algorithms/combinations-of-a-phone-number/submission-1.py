class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        key = [0, 0, ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k',  'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        if len(digits) == 0:
            return []

        def backtrack(curr, ind):
            # print(curr)
            if len(curr) == len(digits):
                res.append(curr)
                return
            # print(digits[ind])
            # print(key[int(digits[ind])])
            for ch in key[int(digits[ind])]:
                backtrack(curr + ch, ind + 1)

        backtrack("", 0)
        return res
