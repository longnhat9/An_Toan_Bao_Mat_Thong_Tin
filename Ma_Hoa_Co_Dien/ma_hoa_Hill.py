#Mã hóa Hill

str_ky_tu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ban_ro = "PAYMOREMONEY"
ban_ro = ban_ro.upper()
key = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]
m = len(key)
ban_ma = ""

size_c = int(len(ban_ro) / m)
index_ban_ro = 0
arr_p = []
arr_ky_tu = []
for i in str_ky_tu :
  arr_ky_tu.append(i)

for i in range(0, size_c) :
  p = []
  count = 0
  while(count < 3) :
    for index_str_ky_tu in range(0, len(str_ky_tu)) :
      if ban_ro[index_ban_ro] == str_ky_tu[index_str_ky_tu] :
        p.append(index_str_ky_tu)
        break
    count = count + 1
    index_ban_ro = index_ban_ro + 1
  arr_p.append(p)

c = ""

for index_p in range(0, len(arr_p)) :
  for index_arr_k in range(0, m) :
    sum = 0
    for index_k_p in range(0, m) :
      tich = key[index_arr_k][index_k_p] * arr_p[index_p][index_k_p]
      sum = sum + tich
    mod = sum % 26
    for i in range(0, len(arr_ky_tu)) :
      if mod == i :
        c = c + arr_ky_tu[i]

print(c)