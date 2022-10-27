#Mã hóa Playfair
def lower_to_upper(arr) :
  for i in range(0, len(arr)) :
    if arr[i].islower() == True:
      arr[i] = arr[i].upper()
  return arr

def tao_arr_char(string_ky_tu) :
  arr_char = []
  length_str = len(string_ky_tu)
  for i in range(0, length_str) :
    arr_char.append(string_ky_tu[i])
  return arr_char

str_ky_tu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr_character = tao_arr_char(str_ky_tu)

ban_ma = "HELLOONEANDALL"
key = "THEDIEIS"
arr_ban_ma = tao_arr_char(ban_ma)
arr_ban_ma = lower_to_upper(arr_ban_ma)
arr_key = tao_arr_char(key)
arr_key = lower_to_upper(arr_key)

n = 5
arr_key_value_trung = []
arr_key_value_khong_trung = []
for i in range(0, len(arr_key) - 1) :
  for k in range(i + 1, len(arr_key)) :
    if arr_key[i] == arr_key[k] :
      arr_key_value_trung.append(arr_key[i])
      continue

for i in range(0, len(arr_key)) :
  for k in arr_key_value_trung :
    if arr_key[i] == k :
      arr_key_value_khong_trung.append(arr_key[i])
  arr_key_value_khong_trung.append(arr_key[i])
print(arr_key_value_khong_trung)