def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    A = str(A)
    aLength = len(A)
    B = str(B)
    bLength = len(B)
    n = A[0] * aLength
    first = int(A[0])
    if int(n) >= int(A):
      first = int(A[0])
    else:
      if A[0] == 9:
        first = 1
        aLength += 1
      else:
        first += 1
    n = B[0] * bLength
    second = int(B[0])
    if int(n) <= int(B):
      second = int(B[0])
    else:
      if B[0] == 1:
        second = 9
        bLength -= 1
      else:
        second -= 1
    res = 0
    while aLength < bLength:
      res += 10 - first
      first = 1
      aLength += 1
    if first == second:
      res += 1
    else:
      res += second - first + 1
    return res