class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for num in nums:
            maxheap.append(-1 * num)
        heapq.heapify(maxheap)
        while k > 0:
            curr = heapq.heappop(maxheap)

            k -= 1
        return -1 * curr

