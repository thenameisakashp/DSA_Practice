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