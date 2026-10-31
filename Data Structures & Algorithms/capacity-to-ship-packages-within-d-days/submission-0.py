class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        mincapacity = r
        while l < r:

            capacity = (r - l) // 2 + l
            day = 1
            curr = 0
            for package in weights:
                if curr + package <= capacity:
                    curr += package
                else:
                    day += 1
                    curr = package
                    if day > days:

                        break
            if day <= days:
                mincapacity = capacity
                r = capacity
            else:
                if l == capacity:
                    break
                l = capacity

        return mincapacity
