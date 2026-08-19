class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def backtrack(curr, open, close):
            if close > open:
                return
            
            if len(curr) == 2 * n:
                if open == close:
                    res.append(curr)
                return
            
            # + )
            backtrack(curr + ")", open, close + 1)

            # + (
            backtrack(curr + "(", open + 1, close)





        backtrack("", 0, 0)
        return res