from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        comparer = min(strs, key=len)

        for w in strs:
            for i in range(len(comparer)):
                if w[i] != comparer[i]:
                    comparer = comparer[:i]
                    break

        return comparer