class Solution:
    def findLength(self, text1: List[int], text2: List[int]) -> int:
        temp1 = len(text1)
        temp2 = len(text2)
        max_length = 0
        dic = [[0 for i in range(temp2 + 1)] for i in range(temp1 + 1)]
        for i in range(1, temp1 + 1):
            for j in range(1, temp2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dic[i][j] = 1 + dic[i - 1][j - 1]
                    max_length = max(max_length,dic[i][j])
                else:
                    dic[i][j] = 0        
        return max_length
