class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        index_start = 0
        index = 0
        no_double_slashes = path[0]
        # slashes
        for i in range(1, len(path)):
            if path[i - 1] == "/" and path[i] == "/":
                continue
            else:
                no_double_slashes += path[i]

        path = no_double_slashes
        if path[-1] != "/":
            path += '/'
        curr = '/'
        for i in range(1, len(path)):
            if path[i] == "/":
                if curr == "/..":
                    if stack:
                        stack.pop()
                    curr = "/"
                elif curr == "/.":
                    curr = "/"
                else:
                    stack.append(curr)
                    curr = "/"
            else:
                curr += path[i]
        ans = ''
        for s in stack:
            ans += s
        return ans if ans else "/"