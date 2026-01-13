from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {}
        inDegrees = [0] * numCourses 
        for a, b in prerequisites:
            if b not in courseMap:
                courseMap[b] = []
            courseMap[b].append(a)
            inDegrees[a] += 1
        stack = []
        for index,inDegree in enumerate(inDegrees):
            if inDegree == 0:
                stack.append(index)
        while stack:
            index = stack.pop()
            for next in courseMap.get(index, []):
                inDegrees[next] -= 1
                if inDegrees[next] == 0:
                    stack.append(next)
        return all(deg == 0 for deg in inDegrees)