class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique_word = []
        unique_count = 0
        for i in words:
            con = ''
            for j in i:
                con += morse[ord(j.lower())-97]
            if con not in  unique_word:
                unique_word.append(con)
                unique_count += 1
        
        return unique_count


# ai 
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
                 "-","..-","...-",".--","-..-","-.--","--.."]
        
        unique_word = set()

        for word in words:
            con = ""
            for ch in word:
                con += morse[ord(ch) - 97]
            unique_word.add(con)

        return len(unique_word)
