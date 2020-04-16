''' площадь круга = 2ПR, площадь прямоугльника = a*b,
 треуг =pow(p(p-a)(p - b)(p-c)). p =(a+b+c)/2.
 '''

operation = input()
if operation == 'круг':
	r = float(input())
	pi = float(3.14)
	print(float((r ** 2) * pi))
if operation == 'прямоугольник':
	a = float(input())
	b = float(input())
	print(a * b)
if operation == 'треугольник':
	a = float(input())
	b = float(input())
	c = float(input())
	p = float((a + b + c) / 2)
	s = float(p(p - a)(p - b)(p - c))
	print(float(pow(s, 0.5)))



'''	a = float(input())
	b = float(input())
	c = float(input())
	r = float(input())
	pi = float(3.14)
	p = float((a + b + c) / 2)
	s = float(p(p - a)(p - b)(p - c))
	if operation == 'прямоугольник':
		print(a * b)
	if operation == 'треугольник':
		print(float(pow(s, 0.5)))
	if operation == 'круг':
		print(float((r ** 2) * pi))
	else:
    	print('ytdthyjt ltqcndbt')'''
