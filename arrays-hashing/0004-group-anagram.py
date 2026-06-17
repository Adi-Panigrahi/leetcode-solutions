class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = { }
        for words in str:
            key = "".sorted(words)
            if words not in group:
                group[key] = [ ]
            group[key].append(words)
        return list(group.values())
            