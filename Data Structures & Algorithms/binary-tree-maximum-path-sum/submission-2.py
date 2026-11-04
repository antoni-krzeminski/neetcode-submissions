class Solution:

  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    max_sum = float("-inf")

    def get_max_gain(node: Optional[TreeNode]) -> int:
      nonlocal max_sum
      if not node:
        return 0

      # 1. Oblicz maksymalny zysk z lewego i prawego poddrzewa.
      # Jeśli zysk jest ujemny, odrzucamy go (bierzemy 0).
      left_gain = max(get_max_gain(node.left), 0)
      right_gain = max(get_max_gain(node.right), 0)

      # 2. Sprawdź sumę ścieżki "zakręcającej" w bieżącym węźle.
      # To jest potencjalny kandydat na globalne maksimum.
      current_path_sum = node.val + left_gain + right_gain
      max_sum = max(max_sum, current_path_sum)

      # 3. Do rodzica możemy oddać TYLKO JEDNĄ odnogę + wartość bieżącego węzła.
      return node.val + max(left_gain, right_gain)

    get_max_gain(root)
    return max_sum
