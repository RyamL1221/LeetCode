# Runtime 37ms (43.80%), Memory: 13.64MB (5.34%)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_note_letters = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] not in ransom_note_letters:
                ransom_note_letters[ransomNote[i]] = 1
            else: 
                ransom_note_letters[ransomNote[i]] += 1
        
        for i in range(len(magazine)):
            if magazine[i] in ransom_note_letters:
                ransom_note_letters[magazine[i]] -= 1
        
        for key, value in ransom_note_letters.items():
            if value > 0:
                return False
        
        return True
        
