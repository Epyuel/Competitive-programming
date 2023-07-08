class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(s) < len(p):
            return []
        dic = {}
        for c in p:
            dic[c] = dic.get(c, 0) + 1
        valid_count = 0 
        count = { k:0 for k in dic }
        res = []
        for i in range(len(p)):
            if s[i] in count:
                if 0 <= count[s[i]] < dic[s[i]]:
                    valid_count += 1
                count[s[i]] += 1
        if valid_count == len(p):
            res.append(0)
        
        for rgt in range(len(p), len(s)):
            lft = rgt - len(p)

            if s[lft] in count:
                if 0 < count[s[lft]] <= dic[s[lft]]:
                    valid_count -= 1
                count[s[lft]] -= 1
            
            if s[rgt] in count:
                if 0 <= count[s[rgt]] < dic[s[rgt]]:
                    valid_count += 1
                count[s[rgt]] += 1
            if valid_count == len(p):
                res.append(lft + 1)

        return res
