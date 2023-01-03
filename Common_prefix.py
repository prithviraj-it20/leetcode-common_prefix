class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        size=len(strs)
        end = min(len(strs[0]), len(strs[size - 1]))
        if(size==0):
            return ""
        elif(size==1):
            return strs[0]
        else:
            i=0
            while(i<end and (strs[0][i]==strs[-1][i])):
                i+=1
            return strs[0][:i]
