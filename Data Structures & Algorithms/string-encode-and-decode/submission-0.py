class Solution:
    delimeter = ";;;;"

    def encode(self, strs: List[str]) -> str:
        return self.delimeter.join(s for s in strs)

    def decode(self, s: str) -> List[str]:
        return s.split(self.delimeter)
