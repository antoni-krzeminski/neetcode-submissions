class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we will keep top k nums in meanheap so that on the top 
        # is the kth largest
        minheap = []
        for num in nums:
            heapq.heappush(minheap, num)
            if len(minheap) > k:
                heapq.heappop(minheap)

        return minheap[0] if nums else -1