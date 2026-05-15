def func(N):
    if N == 0:
        return 1
    return N+func(N-1)
print(func(5))