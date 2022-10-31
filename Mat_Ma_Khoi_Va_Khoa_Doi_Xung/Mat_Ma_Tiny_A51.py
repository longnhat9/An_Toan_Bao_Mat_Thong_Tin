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

def quay_X_or_Y_or_Z(arr, t) :
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

# Bước 0
arr_tinh_t = [x[2], x[4], x[5]]
t_X = phep_tinh_xor(arr_tinh_t)
m = maj(x[1], y[3], z[3])

if x[1] == m :
  x = quay_X_or_Y_or_Z(x, t_X)
if y[3] == m :
  y = quay_X_or_Y_or_Z(y, t_Y)
if z[3] == m :
  z = quay_X_or_Y_or_Z(z, t_Z)

s.append(phep_tinh_xor(arr_tinh_t))

# Bước 1
arr_tinh_t = [y[6], y[7]]
t_Y = phep_tinh_xor(arr_tinh_t)
m = maj(x[1], y[3], z[3])

if x[1] == m :
  x = quay_X_or_Y_or_Z(x, t_X)
if y[3] == m :
  y = quay_X_or_Y_or_Z(y, t_Y)
if z[3] == m :
  z = quay_X_or_Y_or_Z(z, t_Z)

s.append(phep_tinh_xor(arr_tinh_t))

# Bước 2
arr_tinh_t = [z[2], z[7], z[8]]
t_Z = phep_tinh_xor(arr_tinh_t)
m = maj(x[1], y[3], z[3])

if x[1] == m :
  x = quay_X_or_Y_or_Z(x, t_X)
if y[3] == m :
  y = quay_X_or_Y_or_Z(y, t_Y)
if z[3] == m :
  z = quay_X_or_Y_or_Z(z, t_Z)

s.append(phep_tinh_xor(arr_tinh_t))

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

for i in range(0, len(str_ky_tu)) :
  if i == sum :
    print(str_ky_tu[i])
    break