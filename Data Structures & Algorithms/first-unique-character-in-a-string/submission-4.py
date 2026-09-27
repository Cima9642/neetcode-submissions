class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Dictionary to keep track of the frequency of each character
        count = defaultdict(int)  # Maps character -> occurrence count

        # First pass: Count the occurrences of every character in the string
        for c in s:
            count[c] += 1
            
        # Second pass: Iterate through the string with indices to find the first unique character
        for i, c in enumerate(s):
            # If the character's frequency is 1, it's unique; return its index
            if count[c] == 1:
                return i
                
        # If no unique character is found after checking the whole string, return -1
        return -1






        