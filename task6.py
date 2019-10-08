a = int(input())
while a < 1 or a > 999:
  a = int(input())
b = ""
c = "четное "
n = "нечетное "
o1 = "однозначное "
o2 = "двузначное "
o3 = "трехзначное "
if a % 2 == 0:
  b += c
else:
  b += n
if a // 100 > 0:
  b += o3
elif a // 10 > 0:
  b += o2
else:
  b += o1
print(b+"число")
