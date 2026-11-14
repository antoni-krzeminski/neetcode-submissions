class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right = []
        left = []
        for a in asteroids:
            if a > 0:
                right.append(a)
            else:
                exploded = 0
                a = -a
                while right:
                    if a ==  right[-1]:
                        right.pop()
                        exploded = 1
                        break
                    elif a > right[-1]:
                        right.pop()
                    else:
                        break
                if not right and exploded == 0:
                    left.append(-a)
        return left + right

                    
