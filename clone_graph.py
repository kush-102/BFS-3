"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.map = {}

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        q = [node]
        self.map[node] = Node(node.val)
        while q:
            curr = q.pop(0)
            for neigh in curr.neighbors:
                if neigh not in self.map:
                    self.map[neigh] = Node(neigh.val)
                    q.append(neigh)
                self.map[curr].neighbors.append(self.map[neigh])
        return self.map[node]


# time complexity is O(V+E)
# space complexity is O(V+E)
