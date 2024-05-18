def divide(n1, n2):
    return n1 // n2, n1 % n2


print(*divide(int(input()), int(input())), sep='\n')