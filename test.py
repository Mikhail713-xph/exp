a = int(input())
b = int(input())
i = 1
while i <= ( a * b):
    i += 1
    if i % a == 0 and i % b == 0:
        print(i) 
        break