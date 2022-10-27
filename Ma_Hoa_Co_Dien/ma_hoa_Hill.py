#Mã hóa Hill

import numpy as np

dimension = 3
key = np.matrix([[17, 17, 5], [21, 18, 21], [2, 2, 19]])

ban_ro = 'PAYMOREMONEY'
str_ky_tu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ban_ma = ""

for index, i in enumerate(ban_ro):
  values = []
  if index % dimension == 0:
    for j in range(0, dimension):
      if(index + j < len(ban_ro)):
        values.append([str_ky_tu.index(ban_ro[index + j])])
    vector = np.matrix(values)
    vector = key * vector
    vector %= 26
    for j in range(0, dimension):
      ban_ma += str_ky_tu[vector.item(j)]

print(ban_ma)