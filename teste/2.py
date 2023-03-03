# Função que verifica se um número está na sequência de Fibonacci
def pertence_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

# Entrada do usuário
num = int(input("Digite um número: "))

# Cálculo da sequência de Fibonacci
fib = [0, 1]
while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])

# Verificação se o número pertence à sequência
if num in fib:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")