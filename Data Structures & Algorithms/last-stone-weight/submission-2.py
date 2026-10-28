class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap = stones
        # we have only minheap in python so we make num[i] = - num[i]
        for i, num in enumerate(minheap):
            minheap[i] = -1 * num
        heapq.heapify(minheap)

        while len(minheap) > 1:
            x = heapq.heappop(minheap) # heaviest
            y = heapq.heappop(minheap) # heaviest or second to heaviest
            if x == y:
                continue # both destryed
            else:
                heapq.heappush(minheap, x - y) # x is always greater
        
        return -1 * minheap[0] if minheap else 0