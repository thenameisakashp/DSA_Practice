'''n = 1542     #palindrome number
num = n
result=0
while num > 0:
    last_digit = num % 10
    result=(result*10)+last_digit
    num = num // 10
print(result)
print(f"Is {n} a palindrome? {n == result}")'''


'''text="gadag"     #polyndrome string
if text==text[::-1]:
    print("palindrome")'''