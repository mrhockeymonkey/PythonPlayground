
num = 6427
prime = True

for test in range(2,num) :
	if num % test == 0 and num != test:
		prime = False
		print(num, 'equals', test, '*', int(num/test))
		break
		
print('#########################')
if prime :
	print(num, 'is prime')
else :
	print(num, 'is not prime')
print('#########################')
