p = "положительное "
o = "отрицательное "
c = "четное "
n = "нечетное "
z = "нулевое "
b = int(input())
a = ""
if b == 0:
  a += z
else:
  if b < 0:
    a += o
  else:
    a += p
  if b % 2 == 0:
    a += c
  else:
    a += n
print(a+число)
