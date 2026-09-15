class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = 0
        if len(strs) == 1:
            return strs[0]
        elif "" in strs:
            return ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                try:
                    if strs[j-1][i] != strs[j][i]:
                        return strs[0][:out]
                except:
                    return strs[0][:out]
            else:
                out += 1
        return strs[0][:out]
