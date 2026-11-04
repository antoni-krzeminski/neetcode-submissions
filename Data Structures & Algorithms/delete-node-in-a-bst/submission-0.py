class Solution:

  def deleteNode(
      self, root: Optional[TreeNode], key: int
  ) -> Optional[TreeNode]:
    if not root:
      return None

    # 1. Szukamy węzła w odpowiednim poddrzewie
    if key < root.val:
      root.left = self.deleteNode(root.left, key)
    elif key > root.val:
      root.right = self.deleteNode(root.right, key)
    else:
      # Znaleźliśmy węzeł do usunięcia: root.val == key

      # Przypadek 1: Brak lewego dziecka (w tym liść)
      if not root.left:
        return root.right

      # Przypadek 2: Brak prawego dziecka
      if not root.right:
        return root.left

      # Przypadek 3: Dwoje dzieci
      # Szukamy najmniejszego węzła w prawym poddrzewie
      curr = root.right
      while curr.left:
        curr = curr.left

      # Podmieniamy wartość
      root.val = curr.val

      # Rekurencyjnie usuwamy skopiowany węzeł z prawego poddrzewa
      root.right = self.deleteNode(root.right, curr.val)

    return root
