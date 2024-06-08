def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  count = 0
  for i in range(len(R) - 1, 0, -1):
    if R[i] <= R[i - 1]:
      R[i - 1] = R[i] - 1
      if R[i - 1] <= 0:
        return -1
      count += 1
  return count