x = float(input())
while x == 0:
  x = float(input())
y = float(input())
while y == 0:
  y = float(input())
if x > 0 and y > 0:
  print("1")
elif x < 0 and y > 0:
  print("2")
elif x < 0 and y < 0:
  print("3")
elif x > 0 and y < 0:
  print("4")
