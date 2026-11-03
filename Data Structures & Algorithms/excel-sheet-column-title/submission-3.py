class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        print(chr(65))
        ans = ""



        while columnNumber > 26:
            ans = chr(columnNumber % 26 + 64) + ans
            columnNumber = columnNumber // 26
        
        return  chr(columnNumber + 64) + ans
