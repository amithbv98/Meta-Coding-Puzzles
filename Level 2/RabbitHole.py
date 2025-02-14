def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
  L = [0]+L
  dp = [0 for i in range(N +1)]
  visited = set()
  for i in range(1,N+1):
      stack = []
      k = i
      while k not in visited and len(visited) != N:
        stack.append(k)
        visited.add(k)
        k = L[k]
      c = len(stack)
      if dp[k] == 0:
        temp = []
        for j in range(len(stack)-1,-1,-1):
          if stack[j] != k:
            temp.append(stack[j])
          else:
            temp.append(stack[j])
            break
        c = len(temp)
        flag = False
        b = 1
        while stack:
          if not flag:
            if stack[-1] == k:
              flag = True
            dp[stack.pop()] = c
          else:
            dp[stack.pop()] = c + b
            b += 1
      else:
        count = 1
        while stack:
          dp[stack.pop()] = dp[k] + count
          count += 1
  return max(dp)