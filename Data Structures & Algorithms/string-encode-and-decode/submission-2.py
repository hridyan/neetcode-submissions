class Solution:

    def encode(self, strs: list[str]) -> str:
        # Edge Case 1: Empty list returns an empty string
        if not strs:
            return ""
            
        res = []
        for w in strs:
            # Prefix each string with its length and a delimiter (e.g., #)
            res.append(f"{len(w)}#{w}")
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        # Edge Case 1: Empty string decoded back to empty list
        if not s:
            return []
            
        res = []
        i = 0
        
        while i < len(s):
            # Find the delimiter to get the boundaries of the length prefix
            j = i
            while s[j] != '#':
                j += 1
            
            # Read the length of the upcoming string
            length = int(s[i:j])
            
            # Extract the exact string based on the parsed length
            # j + 1 skips the '#' character
            res.append(s[j + 1 : j + 1 + length])
            
            # Move index past the current string to process the next one
            i = j + 1 + length
            
        return res
