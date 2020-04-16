a = int(input())
b = int(input())
c = int(input())

if (a >= b) and (a >= c ) and (b >= c):
	print(a,c,b,sep='\n')

elif (a >= b) and (a >= c ) and (c >= b):
	print(a,b,c,sep='\n')

elif (b >= a) and (b >= c ) and (a >= c):
	print(b,c,a,sep='\n')

elif (b >= a) and (b >= c ) and (c >= a):
	print(b,a,c,sep='\n')


elif (c >= b) and (c >= a ) and (b >= a):
	print(c,a,b,sep='\n')

elif (c >= b) and (c >= a ) and (a >= b):
	print(c,b,a,sep='\n')

else:
	print('nothing')


'''Напишите программу, которая получает на вход три целых числа, 
по одному числу в строке, и выводит на консоль в три строки сначала максимальное,
 потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа. '''