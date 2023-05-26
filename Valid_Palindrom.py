class Solution:
    def isPalindrome(self, s: str) -> bool:
        substitute=re.sub('[\W_]',"",s.lower())
        rev_substitute=substitute[::-1]
        if substitute==rev_substitute:
            return True
        else:
            return False
