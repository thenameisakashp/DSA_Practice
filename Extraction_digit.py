n = 5873      #extraction of digits
num = n
while num > 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10