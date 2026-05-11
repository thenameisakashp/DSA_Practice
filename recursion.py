'''count = 0         #head recursion
def func():
    global count
    if count == 4:
        return
    print("Akash")
    count += 1
    func()
func()'''

'''count = 0         #tail recursion
def func():
    global count
    if count == 4:
        return
    count += 1
    func()
    print("Akash")
func()'''


'''def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))'''