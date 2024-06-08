def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  queue = []
  d = {}
  l = 0
  res = 0
  for item in D:
    d[item] = 0
  for item in D:
    if d[item] == 0:
      res += 1
      if l < K:
        queue.append(item)
        d[item] = 1
        l += 1
      else:
        d[queue[0]] = 0
        queue.pop(0)
        queue.append(item)
        d[item] = 1
        
  return res