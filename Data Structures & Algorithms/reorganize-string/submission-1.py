class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(maxheap)
        ans = ""
        while maxheap:
            x = heapq.heappop(maxheap)
            if len(ans) >= 1 and ans[-1] == x[1]:
                if maxheap == []:
                    return ""
                y = heapq.heappop(maxheap)
                ans += y[1]
                if y[0] + 1 != 0:
                    heapq.heappush(maxheap, (y[0] + 1, y[1]))
                heapq.heappush(maxheap, x)
                continue
            ans += x[1]
            if x[0] + 1 != 0:
                heapq.heappush(maxheap, (x[0] + 1, x[1]))  
        return ans