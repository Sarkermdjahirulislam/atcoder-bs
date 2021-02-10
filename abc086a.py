#abc086a

s = input()
token = s.split()
b = int(token[0])
c = int(token[1])

if (b*c)%2 == 0:
    print('Even')
else:
    print('Odd')
