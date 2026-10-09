class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = "".join(f"{len(s)}#{s}" for s in strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        word = ""
        start = False
        for i in range(len(s)):
            if s[i].isdigit():
                wc = s[i]
                start = True
                if word != "" and len(word) == int(wc):
                    result.append(word)
                continue

            if s[i] == "#" and start == True:
                word = ""
                start = False
                continue
            
            word += s[i]
        

        result.append(word)

        return result

