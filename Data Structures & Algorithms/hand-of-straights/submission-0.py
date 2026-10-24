

class Solution:

  def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
      return False

    counts = Counter(hand)

    # Sort the cards so we always start with the smallest available
    for card in sorted(counts):
      if counts[card] > 0:
        needed = counts[card]
        # Every group starting at 'card' needs card, card+1, ..., card+groupSize-1
        for next_card in range(card, card + groupSize):
          if counts[next_card] < needed:
            return False
          counts[next_card] -= needed

    return True
