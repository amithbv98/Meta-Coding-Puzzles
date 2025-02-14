def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  d = {}
  res = 0
  count = 0
  for item in D:
    if item not in d:
      d[item] = count
      count += 1
      res += 1
    elif d[item] < count - K:
      res += 1
      d[item] = count
      count += 1
  return res
