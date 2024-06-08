def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:

  cur = 1
  sum = 0
  for i in range( len(C)):
    now = C[i]
    sum += min(abs(now - cur), min(now - 1, N - now + 1) + min(cur - 1, N - cur + 1))
    cur = C[i]
  return sum