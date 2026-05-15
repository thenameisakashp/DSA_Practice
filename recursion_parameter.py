'''def func(x,N):  #recursion using parameter
    if N == 0:
        return
    print(x)
    func(x,N-1)
func(15,4)'''

'''def func(i,N):  # head recursion using parameter to print 1 to N
    if i > N:
        return
    print(i)
    func(i+1,N)
func(1,4)'''

'''def func(i,N):  # tail recursion using parameter to print N to 1
    if i > N:
        return
    func(i+1,N)
    print(i)
func(1,4)'''

'''def func(N):  # head recursion using parameter to print N to 1
    if N == 0:
        return
    print(N)
    func(N-1)
func(4)'''


'''def func(N):  # tail recursion using parameter to print 1 to N
    if N == 0:
        return
    func(N-1)
    print(N)

func(4)'''

def func(sum,i,N): #sum of numbers from 1 to N
    if i > N:
        print(sum)
        return
    func(sum+i,i+1,N)

func(0,1,5)
