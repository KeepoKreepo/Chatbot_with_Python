a = int(input())
b = int(input())
h = int(input())

if a <= h <= b:
    print('Normal')
elif h <= a:
    print('Deficiency')
elif b<= h:
    print('Excess')