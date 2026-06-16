class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for chr in s:
            if chr.isalnum():
                cleaned+=chr.lower()
        return cleaned==cleaned[::-1]
    