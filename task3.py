xa = float(input())
ya = float(input())
xb = float(input())
yb = float(input())
xc = float(input())
yc = float(input())
ab = ((xa-xb)**2+(ya-yb)**2)**0.5
ac = ((xa-xc)**2+(ya-yc)**2)**0.5
if ab < ac:
  print("B "+str(ab))
elif ac > ab:
  print("C "+str(ac))
