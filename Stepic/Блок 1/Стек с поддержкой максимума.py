import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        number = int(command[1])
        stack.append(max(stack[-1], number) if stack else number)
    elif command[0] == 'pop':
        stack.pop()
    elif command[0] == 'max':
        print(stack[-1])