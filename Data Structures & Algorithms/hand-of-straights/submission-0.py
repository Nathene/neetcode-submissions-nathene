class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if (len(hand) % groupSize) != 0 :
            return False
        count = Counter(hand)

        hand.sort()

        def exists(i: int) -> bool:
            for j in range(i, i + groupSize):
                if count[j] <= 0:
                    return False
                count[j] -= 1
            return True
        
        for card in hand:
            if count[card] > 0:
                if not exists(card):
                    return False
        
        return True