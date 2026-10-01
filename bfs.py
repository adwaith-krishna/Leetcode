from collections import deque

class Solution:
    def bfs(self, graph: dict,start:int) -> list[int]:
        queue = deque()
        queue.append(start)
        visit=[0]*len(graph)+[0]
        res=set()
        while queue:
            node=queue.popleft()
            res.add(node)
            for neighbour in graph[node]:
                if visit[neighbour]==0:
                    visit[neighbour]=1
                    queue.append(neighbour)

        return res

        



a=Solution()

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 7],
    6: [3, 8],
    7: [5, 9],
    8: [6],
    9: [7]
}
start=1
print(a.bfs(graph,start))