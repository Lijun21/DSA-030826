"""
648 Redundant Connect

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
The graph is represented as an array edges of length n where edges[i] = [ai, bi] 
indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
If there are multiple answers, return the answer that occurs last in the input.

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

1-2
| /
3

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

"""
class DSU:
    def __init__(self, n:int)->None:
        self.parent = [i for i in range(n)]
        self.size = [1]*n
       
    #p [1,1,2]
    #s [1,2,1]
    # check two nodes are in the same group, in nearly constant time, 
    # inverse Ackermann function
    def find(self, node:int)->int:
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a:int, b:int)->bool: # 0, 1
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            # set pb's parent to be pa, add smaller into bigger group
            self.parent[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            # set pa's parent to be pb
            self.parent[pa] = pb
            self.size[pb] += self.size[pa]
        return True

def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    nodes_count = len(edges)
    # initilize dsu, n nodes
    dsu = DSU(nodes_count)

    for a, b in edges:
        if not dsu.union(a-1, b-1):
            return [a, b]



edges1 = [[1,2],[1,3],[2,3]]
print(findRedundantConnection(edges1)) # Output: [2,3]

edges2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(findRedundantConnection(edges2)) # Output: [1,4]