#Mã hóa Vigenere

def tao_arr_char(string_ky_tu) :
  arr_char = []
  length_str = len(string_ky_tu)
  for i in range(0, length_str) :
    arr_char.append(string_ky_tu[i])
  return arr_char

def arr_to_string(arr) :
  str = ""
  for i in arr :
    str = str + i
  return str

def lower_to_upper(arr) :
  for i in range(0, len(arr)) :
    if arr[i].islower() == True:
      arr[i] = arr[i].upper()
  return arr

str_ky_tu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length_str = len(str_ky_tu)
arr_char = []
arr_phu = []
arr_chinh = []

arr_char = tao_arr_char(str_ky_tu)
arr_chinh.append(arr_char)
arr_phu = tao_arr_char(str_ky_tu)

while True :
  arr_new = []
  template = arr_phu[0]
  for i in range(0, length_str - 1) :
    arr_phu[i] = arr_phu[i + 1]
    arr_new.append(arr_phu[i])
  arr_phu[length_str - 1] = template
  arr_new.append(arr_phu[length_str - 1])
  arr_chinh.append(arr_new)

  if (arr_phu[0] == "Z") :
    break

# Lặp khóa
M = "ALLWORKANDNOPLAYmA"
key = "WhENINRo"
arr_m = tao_arr_char(M)
arr_m = lower_to_upper(arr_m)
arr_key_ban_dau = tao_arr_char(key)
arr_key_ban_dau = lower_to_upper(arr_key_ban_dau)

for i in range(0, len(arr_key_ban_dau)) :
  if arr_key_ban_dau[i].islower() == True:
    arr_key_ban_dau[i] = arr_key_ban_dau[i].upper()
arr_key = tao_arr_char(key)
arr_key = lower_to_upper(arr_key)
arr_c = []

if(len(key) < len(M)) :
  do_dai_con_thieu = len(M) - len(key)
  for i in range(0, do_dai_con_thieu) :
    for k in arr_key_ban_dau :
      if len(arr_key) < len(arr_m) :
        arr_key.append(k)
      else :
        break

for i in range(0, len(arr_m)) :
  index_m = arr_chinh[0].index(arr_m[i])
  index_key = arr_chinh[0].index(arr_key[i])
  arr_c.append(arr_chinh[index_m][index_key])

C = arr_to_string(arr_c)
print(C)