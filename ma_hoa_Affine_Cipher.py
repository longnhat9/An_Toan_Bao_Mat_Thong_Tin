#Mã tuyến tính Affine Cipher

def lower_to_upper(arr) :
  for i in range(0, len(arr)) :
    if arr[i].islower() == True:
      arr[i] = arr[i].upper()
  return arr

str_ky_tu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def tao_arr_char(string_ky_tu) :
  arr_char = []
  length_str = len(string_ky_tu)
  for i in range(0, length_str) :
    arr_char.append(string_ky_tu[i])
  return arr_char

arr_character = tao_arr_char(str_ky_tu)

#Cho khóa k = (5, 6) => a = 5 , b = 6
a = 5
b = 6

#Kiểm thử xem gcd(a, 26) = 1 hay ko?
#Ước số chung lớn nhất của 5 và 26 = 1 => thỏa mãn yêu cầu để giải mã
#Ta có e(x) = 5x + 6
# y = 5x + 6

ban_ma = "HENTOITHUBAY"
arr_x = []
arr_y = []
arr_ban_ma = tao_arr_char(ban_ma)
arr_ban_ma = lower_to_upper(arr_ban_ma)
for i in arr_ban_ma :
  for k in arr_character :
    if i == k :
      arr_x.append(arr_character.index(i))
      break

for i in arr_x :
  sum = a * i + b
  mod = sum % 26
  arr_y.append(mod)

str_giai_ma = ""

for i in arr_y :
  str_giai_ma = str_giai_ma + arr_character[i]

print(str_giai_ma)