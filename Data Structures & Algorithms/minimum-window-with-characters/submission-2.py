class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or s == "" or t == "":
            return ""
        if s == t:
            return t
        

        substr_chars = {}
        required_chars = {}

        result_boundaries = [None, None]
        result_length = len(s) + 1

        l = 0

        for c in t:
            required_chars[c] = required_chars.get(c, 0) + 1

        have, required = 0, len(required_chars)

        for r in range(len(s)):
            c = s[r]
            substr_chars[c] = substr_chars.get(c, 0) + 1

            if c in required_chars and substr_chars[c] == required_chars[c]:
                have += 1
            
            while have == required:
                if (r - l + 1) < result_length:
                    result_length = r - l + 1
                    result_boundaries = [l, r]
                
                leftmost = s[l]
                substr_chars[leftmost] -= 1
                if leftmost in required_chars and substr_chars[leftmost] < required_chars[leftmost]:
                    have -= 1

                l += 1

        l, r = result_boundaries

        return s[l:r + 1] if result_length != len(s) + 1 else ""

            

        

