'''
A cafeteria table consists of a row of N seats, numbered from 1 to 𝑁 from left to right. Social distancing guidelines require that every diner be seated such that 
K seats to their left and K seats to their right (or all the remaining seats to that side if there are fewer than K) remain empty.
There are currently M diners seated at the table, the ith of whom is in seat 𝑆. No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, 
assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
'''

from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  S.sort()
  sum = 0
  res = [S[0] - 1]
  for i in range(1, len(S)):
    res.append(S[i] - S[i - 1])
  res.append(N - S[-1])
  sum += res[0] // (K+1)
  for i in range(1, len(res) - 1):
    if res[i] // (K + 1) != 0:
       sum += res[i] // (K + 1) - 1    
  sum += res[-1] // (K + 1)
  print(res)
     
  return sum
