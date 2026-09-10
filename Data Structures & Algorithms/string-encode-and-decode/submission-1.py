class Solution:
# i am given an algorithim to encode a list of strings where i need to keep all information about the string inside the encoding
# i can make the char lenght of the string and a special charcter and if this pattern starts from the beginning it would perserver all special chars
    def encode(self, strs: List[str]) -> str:
        ans = []
        for s in strs: 
            ans.append(str(len(s)))
            ans.append("#")
            ans.append(s)
        
        return "".join(ans)

    def decode(self, s: str) -> List[str]:

        #5#Hello5#World
        ans = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j
        return ans


            
