class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = ["(", "[", "{"]
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for x in s:
            if x in openings:
                stack.append(x)
            else:
                if stack and stack[-1] == closeToOpen[x]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
            