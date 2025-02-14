def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  photo = []
  backDrop = []
  count = 0
  for i in range(N):
    if C[i] == 'P':
      count += 1
    photo.append(count)
  count = 0
  for i in range(N):
    if C[i] == 'B':
      count += 1
    backDrop.append(count)
  lphotos = []
  rphotos = []
  lback = []
  rback = []
  for i in range(N):
    if C[i] == 'A':
      if i - X >= 0:
        if i - Y < 0:
          if C[0] == 'P':
            lphotos.append(photo[i - X] - photo[0] + 1)
          else:
            lphotos.append(photo[i - X] - photo[0])
          if C[0] == 'B':
            lback.append(backDrop[i - X] - backDrop[0] + 1)
          else:
            lback.append(backDrop[i - X] - backDrop[0])
        else:
          if C[i - Y] == 'P':
            lphotos.append(photo[i - X] - photo[i - Y] + 1)
          else:
            lphotos.append(photo[i - X] - photo[i - Y])
          if C[i - Y] == 'B':
            lback.append(backDrop[i - X] - backDrop[i - Y] + 1)
          else:
            lback.append(backDrop[i - X] - backDrop[i - Y])
      else:
        lphotos.append(0)
        lback.append(0)
      if i + X < N:
        if i + Y >= N:
          if C[i + X] == 'P':
            rphotos.append(photo[N-1] - photo[i + X] + 1)
          else:
            rphotos.append(photo[N - 1] - photo[i + X])
          if C[i + X] == 'B':
            rback.append(backDrop[N-1] - backDrop[i + X] + 1)
          else:
            rback.append(backDrop[N - 1] - backDrop[i + X])
        else:
          if C[i + X] == 'P':
            rphotos.append(photo[i + Y] - photo[i + X] + 1)
          else:
            rphotos.append(photo[i + Y] - photo[i + X])
          if C[i + X] == 'B':
            rback.append(backDrop[i + Y] - backDrop[i + X] + 1)
          else:
            rback.append(backDrop[i + Y] - backDrop[i + X])
      else:
        rphotos.append(0)
        rback.append(0)
            
  ans = 0
  for i in range(len(rphotos)):
    ans += rphotos[i] * lback[i]
    ans += lphotos[i] * rback[i]
  return ans