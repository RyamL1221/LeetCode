# Runtime: O(n log n), 81ms (64.62%); Memory: O(1), 51.42MB (21.55%)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort(key=lambda interval: interval[0])
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                prev_end = min(prev_end, end)
                result += 1
        
        return result
