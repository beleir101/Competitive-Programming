from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True) 
        deck_result = deque()
        for card in deck:
            if len(deck_result)  > 1:
                deck_result.rotate(1)
            deck_result.appendleft(card)
        return list(deck_result)