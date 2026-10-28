class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for i, point in enumerate(points):
            curr = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(minheap, (-curr, point))
            if len(minheap) > k:
                heapq.heappop(minheap)
        return [point for dist, point in minheap]