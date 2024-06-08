def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  ind = []
  l = len(C)
  rPhoto = []
  rBack = []
  for i in range(len(C)):
    if C[i] == 'A':
      ind.append(i)
  print(ind)
  for item in ind:
    c1 = 0
    c2 = 0
    if item + X >= l:
      rPhoto.append(0)
      rBack.append(0)
      continue
    if item + Y >= l:
      t = l
    else:
      t = item + Y + 1
    for i in range(item + X, t):
      if C[i] == 'P':
        c1 += 1
      if C[i] == 'B':
        c2 += 1
    rPhoto.append(c1)
    rBack.append(c2)
  lPhoto = []
  lBack = []
  C = C[::-1]
  ind = []
  for i in range(len(C)):
    if C[i] == 'A':
      ind.append(i)
  for item in ind:
    c1 = 0
    c2 = 0
    if item + X >= l:
      lPhoto.append(0)
      lBack.append(0)
      continue
    if item + X >= l:
      continue
    if item + Y >= l:
      t = l
    else:
      t = item + Y + 1
    for i in range(item + X, t):
      if C[i] == 'P':
        c1 += 1
      if C[i] == 'B':
        c2 += 1
    lPhoto.append(c1)
    lBack.append(c2)
  lPhoto.reverse()
  lBack.reverse()
  sum = 0
  for i in range(len(lPhoto)):
    sum += lPhoto[i] * rBack[i]
    sum += rPhoto[i] * lBack[i
  return sum