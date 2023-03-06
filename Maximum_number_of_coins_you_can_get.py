class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles=sorted(piles,reverse=True)
        n=int(len(piles)/3)
        coins=0
        for i in range(0,(len(piles)-n)-1,2):
            coins+=piles[i+1]
        return coins
