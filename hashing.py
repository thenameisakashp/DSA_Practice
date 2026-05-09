n = [5,8,3,1,5,2,6,6,8]    #hashing technique to count the frequency of elements in a list
m = [10,5,6,8,9,2,1,3,4]
for i in m:
    count = 0
    for num in n:
        if i==num:
            count+=1
    print(count)
