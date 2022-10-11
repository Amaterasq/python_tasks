fib = lambda x: 1 if x <= 2 else fib(x - 1) + fib(x - 2)


# assert fib(31) == 1346269
# assert fib(1) == 1
# assert fib(0) == 1
