from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        symbol_map = defaultdict(int)

        for sw, st in zip(s, t):
            symbol_map[sw] += 1
            symbol_map[st] -= 1

        return all(x == 0 for x in symbol_map.values())
