class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str: 
        maxheap = []
        if a != 0:
            maxheap.append((-a, 'a'))
        if b != 0:
            maxheap.append((-b, 'b'))
        if c != 0:
            maxheap.append((-c, 'c'))


        heapq.heapify(maxheap)


        ans = ""
        while len(maxheap) != 0:
            print(ans, maxheap)

            x = heapq.heappop(maxheap)
            letter = x[1]
            if len(ans) >= 2 and letter == ans[-2] == ans[-1]:
                if len(maxheap) == 0:
                    return ans
                y = heapq.heappop(maxheap)
                letter = y[1]
                newamount = y[0] + 1
                ans = ans + letter
                if newamount != 0:
                    heapq.heappush(maxheap, (newamount, letter))
                heapq.heappush(maxheap, x)
                continue

            newamount = x[0] + 1
            ans = ans + letter
            if newamount != 0:
                heapq.heappush(maxheap, (newamount, letter))
        return ans
