def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  P.sort()
  l = len(P)
  res = 0
  for i in range(1, l):
    res += P[i] - P[i-1] - 1
  res += N - 1 - P[-1]
  return res + l