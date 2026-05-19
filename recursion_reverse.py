'''num = [5, 4, 3, 2, 1]  #simple way to reverse a list
num.reverse()
print(num)'''

'''num =[2,3,5,7,11] #reverse a list using slicing
print(num[::-1])'''

'''def reverse(num):  #reverse a list using recursion
    if len(num) == 0:
        return []
    return [num[-1]] + reverse(num[:-1])
num = [2, 3, 5, 7, 11]
print(reverse(num))'''


num = [2, 3, 5, 7, 11] #reverse a list using recursion and swapping
def reverse(num,left,right):
    if left >= right:
        return num
    num[left], num[right] = num[right], num[left]
    return reverse(num, left + 1, right - 1)

print(reverse(num, 0, len(num)-1))