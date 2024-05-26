def is_palindrome(_sentence: str) -> bool:
        reverse_temp = ""

        for i in range(len(_sentence) -1, -1, -1):
            reverse_temp += _sentence[i]
        
        if _sentence == reverse_temp:
            return True
        
        return False

class Solution:
    
    
    def longestPalindrome(self, _sentence: str) -> str:
        max_length = -1
        output = ""
        
        if len(_sentence) == 1:
            return _sentence
        elif len(_sentence) == 2:
            if _sentence[0] != _sentence[1]:
                return _sentence[0]
        
        for i in range(0, len(_sentence)):
            next_letter = _sentence.find(_sentence[i], i + 1)
            temp = _sentence[i:next_letter + 1]
        
            if is_palindrome(temp):
                if max_length < len(temp):
                    output = temp
                    max_length = len(temp)
        
        return output

