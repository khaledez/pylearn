
# for i in range(1,21):
#     if i % 3 == 0 or i % 5 == 0:
#         if i % 3 == 0:
#             print("Fizz", end='')
#         if i % 5 == 0:
#             print("Buzz", end='')
#         print("")
#     else:
# print(i)


def fib(n):
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)


print([fib(x) for x in range(0, 20)])
