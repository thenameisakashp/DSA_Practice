'''num = 12   #factors of a number(by brut force method)
result = []
for i in range(1,num//2+1):
    if num %i == 0:
        result.append(i)
result.append(num)
print(result)'''


'''from math import sqrt         #optimal way to find factors of a number
num = 36
result = []
for i in range(1,int(sqrt(num)+1)):
    if num %i == 0:
        result.append(i)
        if num//i !=i:
            result.append(num//i)
           
print(sorted(result))'''