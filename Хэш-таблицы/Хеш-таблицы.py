n = int(input())
H = [''] * 10000000
for i in range(n):
    command, number, *name = input().split()
    number = int(number)
    if command == 'add':
        H[number] = name[0]
    if command == 'del':
        H[number] = ''
    if command == 'find':
        print('not found') if H[number] == '' else print(H[number])
