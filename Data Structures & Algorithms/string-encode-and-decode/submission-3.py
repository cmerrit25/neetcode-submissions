class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += str(len(word)) + "#" + word
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        start = 0
        while start < len(s):
            j = start
            while s[j] != "#":
                j += 1
            length = int(s[start:j])
            start = j + 1
            j = start + length
            output.append(s[start:j])
            start = j
        return output