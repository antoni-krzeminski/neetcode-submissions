class Solution:

  def partition(self, s: str) -> list[list[str]]:
    ans = []

    def dfs(start: int, curr: list[str]) -> None:
      # If we reached the end of the string, snapshot the valid         partition
      if start == len(s):
        ans.append(list(curr))
        return

      # Try cutting every possible prefix starting at 'start'
      for end in range(start, len(s)):
        substring = s[start : end + 1]

        # Only continue down this path if the slice is a palindrome
        if substring == substring[::-1]:
          curr.append(substring)  # Choose
          dfs(end + 1, curr)  # Explore remaining string
          curr.pop()  # Unchoose (backtrack)

    dfs(0, [])
    return ans
