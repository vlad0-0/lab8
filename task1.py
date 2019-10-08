a = int(input())
b = int(input())
if a != b:
	a = max(a, b)
else:
	a = 0
b = a
print(a, b)
