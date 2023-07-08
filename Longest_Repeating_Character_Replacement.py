class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l_pointer=0
        r_pointer=0
        dic={}
        max_substring=0
        while l_pointer <= r_pointer and r_pointer<len(s):
            dic[s[r_pointer]]=dic.get(s[r_pointer],0) + 1

            max_dic_value=max(dic.values())
            window_len=r_pointer - l_pointer + 1 
            
            if window_len - max_dic_value > k:
                dic[s[l_pointer]]-=1
                l_pointer+=1
            
            max_substring=max(max_substring,r_pointer - l_pointer + 1)
            r_pointer+=1
        return max_substring

