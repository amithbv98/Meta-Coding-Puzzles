def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  S.sort()
  m = S[-1]
  ans = 0
  flag = False
  if m % 2 == 0:
    ans = m // 2
  else:
    flag = True
    ans = m // 2 + 1
  if flag:
    return ans
  for item in S:
    if item % 2 == 1:
      return ans + 1
  return ans
 
    
  
  return 0