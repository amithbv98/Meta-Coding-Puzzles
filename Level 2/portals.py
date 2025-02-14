def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    queue = deque()
    visited = set()
    k = {}
    start = 0
    for i in range(R):
        for j in range(C):
            if G[i][j] == "E":
                queue.append((i, j))
                visited.add((i, j))
            if G[i][j] in "abcdefghijklmnopqrstuvwxyz":
              if G[i][j] not in k:
                k[G[i][j]] = [(i, j)]
              else:
                k[G[i][j]].append((i, j))
            if G[i][j] == 'S':
              start = (i, j)
    
    d = {}
    steps = 1
    res = []
    # BFS from "E"
    while queue:
        for _ in range(len(queue)):          
            m, n = queue.popleft()
            if G[m][n] in "abcdefghijklmnopqrstuvwxyz":
              for item in k[G[m][n]]:
                if (item[0], item[1]) not in visited:
                  queue.append((item[0], item[1]))
                  visited.add((item[0], item[1]))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # Directional moves
                x, y = m + dx, n + dy
                if 0 <= x < R and 0 <= y < C and G[x][y] != '#' and (x, y) not in visited:
                    if (x, y) == start:
                      res.append(steps)
                      continue
                    queue.append((x, y))
                    visited.add((x, y))                     
        steps += 1
    return -1 if not res else min(res)