a = int(input("Digite o primeiro valor "))
b = int(input("Digite o segundo valor "))
op = input("+: Soma\n-: Subrtração\n*: Multiplicação\n/: Divisão")
if op == '+':
    res = a + b
elif op == '-':
    res = a - b
elif op == '*':
    res = a * b
else:
    res = a // b
print(res)
