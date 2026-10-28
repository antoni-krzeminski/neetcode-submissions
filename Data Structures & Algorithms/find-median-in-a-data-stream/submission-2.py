import heapq


class MedianFinder:

  def __init__(self):
    # Max-heap (przechowuje mniejszą połowę liczb, zanegowane)
    self.small = []
    # Min-heap (przechowuje większą połowę liczb)
    self.large = []

  def addNum(self, num: int) -> None:
    # 1. Zawsze najpierw wrzucamy do small (max-heap)
    heapq.heappush(self.small, -num)

    # 2. Upewniamy się, że każdy element w small <= każdy element w large
    if self.small and self.large and (-self.small[0] > self.large[0]):
      val = -heapq.heappop(self.small)
      heapq.heappush(self.large, val)

    # 3. Balansujemy rozmiary (small może mieć max o 1 element więcej niż large)
    if len(self.small) > len(self.large) + 1:
      val = -heapq.heappop(self.small)
      heapq.heappush(self.large, val)
    elif len(self.large) > len(self.small):
      val = heapq.heappop(self.large)
      heapq.heappush(self.small, -val)

  def findMedian(self) -> float:
    # Jeśli nieparzysta liczba elementów, mediana jest w small
    if len(self.small) > len(self.large):
      return float(-self.small[0])

    # Jeśli parzysta, średnia z wierzchołków obu kopców
    return (-self.small[0] + self.large[0]) / 2.0
