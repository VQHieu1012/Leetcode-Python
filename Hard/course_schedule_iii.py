class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: (x[1], x[0]))
        total = 0
        heap = []
        for duration, deadline in courses:
            total += duration
            heappush(heap, -duration)
        
            if total > deadline:
                total += heappop(heap)
        return len(heap)
    