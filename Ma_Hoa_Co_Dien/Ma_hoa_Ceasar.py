# Mã hóa Ceasar

str_ky_tu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_ky_tu = str_ky_tu.upper()


arr_ky_tu = []
for i in str_ky_tu :
  arr_ky_tu.append(i)

ban_tin = "bettersafethanso"
ban_tin = ban_tin.upper()
key = 5

arr_ky_tu_da_dich_chuyen = []

for i in range(key, len(arr_ky_tu)) :
  arr_ky_tu_da_dich_chuyen.append(arr_ky_tu[i])

for i in range(0, key) :
  arr_ky_tu_da_dich_chuyen.append(arr_ky_tu[i])

arr_ban_tin = []
for i in ban_tin :
  arr_ban_tin.append(i)

ban_ma = []

for i in range(0, len(arr_ban_tin)) :
  for k in range(0, len(arr_ky_tu)) :
    if arr_ban_tin[i] == arr_ky_tu[k] :
      ban_ma.append(arr_ky_tu_da_dich_chuyen[k])
      break

str_ban_ma = ""
for i in ban_ma :
  str_ban_ma = str_ban_ma + i

print(str_ban_ma)