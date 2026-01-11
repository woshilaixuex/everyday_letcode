from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {}
        for list in prerequisites:
            courseMap[list[0]] = list[1]