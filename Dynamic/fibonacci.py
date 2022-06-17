def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    elif n <= 2:
        return 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]

number = int(input("How many fibonacci numbers: "))
for n in range(number):
    print(f'{n + 1}: {fib(n + 1)}')