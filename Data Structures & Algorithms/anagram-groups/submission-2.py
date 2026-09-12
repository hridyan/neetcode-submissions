class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]

        dict = {x:[] for x in set(''.join(sorted(words)) for words in strs)}
        for s in strs:
            dict[''.join(sorted(s))].append(s)
        for key in dict:
            res.append(dict[key])
        
        return res
        