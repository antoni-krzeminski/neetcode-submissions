from collections import Counter
import heapq


class Solution:

  def reorganizeString(self, s: str) -> str:
    count = Counter(s)
    if any(cnt > (len(s) + 1) // 2 for cnt in count.values()):
      return ""

    maxheap = [(-cnt, char) for char, cnt in count.items()]
    heapq.heapify(maxheap)

    ans = []
    while maxheap:
      x = heapq.heappop(maxheap)

      if len(ans) >= 1 and ans[-1] == x[1]:
        if not maxheap:
          return ""
        y = heapq.heappop(maxheap)
        ans.append(y[1])
        if y[0] + 1 != 0:
          heapq.heappush(maxheap, (y[0] + 1, y[1]))
        heapq.heappush(maxheap, x)
        continue

      ans.append(x[1])
      if x[0] + 1 != 0:
        heapq.heappush(maxheap, (x[0] + 1, x[1]))

    return "".join(ans)

