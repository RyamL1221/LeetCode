# Runtime: 6ms (77.87%); Memory: 21.71MB (14.83%)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            if result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        
        return result
