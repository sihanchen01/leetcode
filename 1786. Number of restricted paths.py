from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def countRestrictedPaths(self, n: int, edges) -> int:
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        paths = [0] * (n+1)
        paths[n] = 1
        dists = [-1] * (n+1)
        q = [(0, n)]

        while q:
            dist, node = heappop(q)
            if dists[node] != -1:
                continue

            dists[node] = dist
            for v, w in graph[node].items():
                if dists[v] == -1:
                    heappush(q, (dist + w, v))
                elif dists[v] < dists[node]:
                    paths[node] += paths[v]

            if node == 1:
                return paths[node] % (10**9 + 7)

        return 0


s = Solution()
edges = [[1, 2, 3], [1, 3, 3], [2, 3, 1], [
    1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]]
s.countRestrictedPaths(5, edges)
