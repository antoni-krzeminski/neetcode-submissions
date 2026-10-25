class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_lower_than_target = [0, 0, 0]
        for triplet in triplets:
            possible = True
            for i in range(3):
                if triplet[i] > target[i]:
                    possible = False
                    break
            if not possible :
                continue
            for i in range(3):
                max_lower_than_target[i] = max(max_lower_than_target[i], triplet[i])
        if max_lower_than_target == target:
            return True
        return False