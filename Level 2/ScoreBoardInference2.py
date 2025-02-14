def getMinProblemCount(N: int, S: List[int]) -> int:
    maxVal = max(S)
  
    if maxVal % 3 == 0:
      return maxVal // 3 + int(any(x % 3 != 0 for x in S))
  
    if maxVal % 3 == 1 and 1 not in S and maxVal-1 not in S:
      return maxVal // 3 + 1
  
    return maxVal // 3 + int(any(x % 3 == 1 for x in S)) + int(any(x % 3 == 2 for x in S))