def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
  A.sort()
  B.sort()
  oneRoundTime = 0
  totalTime = 0
  for i in range(len(A)):
    oneRoundTime += B[i] - A[i]
  totalTime += (K // oneRoundTime) * C
  K = K % oneRoundTime
  ind = 0
  cur = 0
  if K == 0:
    return totalTime - (C - B[-1])
  while K > 0:
    totalTime += A[ind] - cur
    totalTime += B[ind] - A[ind]
    cur = B[ind]
    K = K - (B[ind] - A[ind])
    ind += 1
  return totalTime + K