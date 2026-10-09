class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "" or len(s) < len(t):
            return ""
        elif s == t:
            return t

        
        current_count, target_count = 0, len(t)
        current_map, target_map = {}, {}
        left = 0
        result = [-1, -1]
        result_length = len(s) + 1

        for c in t:
            target_map[c] = target_map.get(c, 0) + 1
        
        for right in range(len(s)):
            c = s[right]
            current_map[c] = current_map.get(c, 0) + 1

            if c in target_map and current_map[c] == target_map[c]:
                current_count += 1
            
            while current_count == target_count:
                if len(s[left:right]) < result_length:
                    result_length = len(s[left:right])
                    result = [left, right]
            
                leftmost = s[left]
                current_map[leftmost] -= 1

                if leftmost in target_map and current_map[leftmost] < target_map[leftmost]:
                    current_count -= 1
                
                left += 1
        
        l, r = result

        return s[l:r+1] if target_count != -1 else ""
                    




        

        

