class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        numList = list(range(1, n+1))
        start = 0
        while(len(numList) > 1):
            index = start+k-1 if start+k-1 < len(numList) else (start+k-1)%len(numList)
            print(index)
            del numList[index]
            start = index
        return numList[0]