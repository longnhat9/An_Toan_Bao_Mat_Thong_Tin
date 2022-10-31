#Tiny-A5/1

def phep_tinh_xor(arr) :
  sum = 0
  for i in arr :
    sum = sum + i
    if sum == 2 :
      sum = 0
  return sum

def maj(x, y, z) :
  count = 0
  if x == 0 :
    count = count + 1
  if y == 0 :
    count = count + 1
  if z == 0 :
    count = count + 1
  if count >= 2 :
    return 0
  else :
    return 1

s = []

def quay_X(arr, arr_of_x2_x4_x5) :
  t = phep_tinh_xor(arr_of_x2_x4_x5)
  i = len(arr) - 1
  while i > 0 :
    arr[i] = arr[i - 1]
    i = i - 1
  arr[0] = t
  return arr

def quay_Y(arr, arr_of_x6_x7) :
  t = phep_tinh_xor(arr_of_x6_x7)
  i = len(arr) - 1
  while i > 0 :
    arr[i] = arr[i - 1]
    i = i - 1
  arr[0] = t
  return arr

def quay_Z(arr, arr_of_x2_x7_x8) :
  t = phep_tinh_xor(arr_of_x2_x7_x8)
  i = len(arr) - 1
  while i > 0 :
    arr[i] = arr[i - 1]
    i = i - 1
  arr[0] = t
  return arr

ban_ro = "111"
k = "100101.01001110.100110000"
x = []
y = []
z = []

arr_ban_ro = []
for i in ban_ro :
  arr_ban_ro.append(int(i))

for i in range(0,6) :
  x.append(int(k[i]))
for i in range(7,15) :
  y.append(int(k[i]))
for i in range(16,25) :
  z.append(int(k[i]))

arr_so_quay_x = []
arr_so_quay_y = []
arr_so_quay_z = []

t_X = phep_tinh_xor(arr_so_quay_x)
t_Y = phep_tinh_xor(arr_so_quay_y)
t_Z = phep_tinh_xor(arr_so_quay_z)

s = []

for i in range(0, len(ban_ro)) :
  arr_tinh_t_X = [x[2], x[4], x[5]]
  arr_tinh_t_Y = [y[6], y[7]]
  arr_tinh_t_Z = [z[2], z[7], z[8]]
  m = maj(x[1], y[3], z[3])

  if x[1] == m :
    x = quay_X(x, arr_tinh_t_X)
  if y[3] == m :
    y = quay_Y(y, arr_tinh_t_Y)
  if z[3] == m :
    z = quay_Z(z, arr_tinh_t_Z)
  
  arr_tinh_s = [x[5], y[7], z[8]]
  s.append(phep_tinh_xor(arr_tinh_s))

arr_c = []

for i in range(0, len(arr_ban_ro)) :
  sum = s[i] + arr_ban_ro[i]
  if sum == 2 :
    sum = 0
  arr_c.append(sum)

sum = 0
i = len(arr_c) - 1
mu = 0
while i >= 0 :
  if arr_c[i] == 1:
    sum = sum + 2 ** mu
  i = i - 1
  mu = mu + 1

str_ky_tu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

arr_ky_tu = []
for i in range(0, len(str_ky_tu)) :
  if i == sum :
    print(str_ky_tu[i])
    break