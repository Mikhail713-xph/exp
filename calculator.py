a = float(input('Введите значение №1: '))
b = float(input('Введите значение №2: '))
operation = input('Выберите операцию: +, -, /, *, mod, pow, div: ')
if operation == '+':
    print(a + b)
elif operation == '-':
	print(a - b)
elif (operation == '/') and (b != 0):
	print(a / b)
elif operation == '/' and b == 0:
	print('Деление на 0!')
elif operation == '*':
	print(a * b)
elif (operation == 'mod') and (b != 0):
	print(a % b)
elif (operation == 'mod') and (b == 0):
	print('Деление на 0!')
elif operation == 'pow':
	print(pow(a,b))
elif (operation == 'div') and (b != 0):
	print(a // b)
elif (operation == 'div') and (b == 0):
	print('Деление на 0!')
else:
	print('Выбрнана неверная операция!')