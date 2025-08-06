# Runtime: 21ms (64.55%); Memory: 17.83MB (30.04%)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1:
            result = []
            subarr = []
            subarr.append(strs[0])
            result.append(subarr)
            return result
        result = []
        sorted_strings = []
        visited_strings = {}
        index_groups = []
        for i in range(len(strs)):
            sorted_strings.append("".join(sorted(strs[i])))
        for i in range(len(strs)):
            if sorted_strings[i] not in visited_strings:
                visited_strings[sorted_strings[i]] = []
                visited_strings[sorted_strings[i]].append(i)
            else: 
                visited_strings[sorted_strings[i]].append(i)
        for key in visited_strings:
            mini_result = []
            for i in range(len(visited_strings[key])):
                mini_result.append(strs[visited_strings[key][i]])
            result.append(mini_result)
        return result
