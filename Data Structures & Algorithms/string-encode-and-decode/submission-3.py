class Solution:
    sep = ":"

    def encode(self, strs: List[str]) -> str:
        """
            Input: ["Hello","World"]
            Ouput: "5:Hello5:World"
        """
        return "".join(f"{len(string)}{self.sep}{string}" for string in strs)

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        
        while i < len(s):
            j = i

            while s[j] != self.sep:
                j += 1
            
            length = int(s[i:j])
            string = s[j + 1: j + 1 + length]
            result.append(string)

            i = j + 1 + length

        return result




