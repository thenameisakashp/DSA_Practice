n=252              #armstrong number
num = n
total = 0
nod = len(str(n))
while num > 0:
    ld = num %10
    total =total+(ld**nod)
    num = num//10
if total == n :
    print(f'{n} is an armstrong number')
else:
    print(f'{n} is not an armstrong number')