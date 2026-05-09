'''n = [5,8,3,1,5,2,6,6,8]    #hashing technique to count the frequency of elements in a list
m = [10,5,6,8,9,2,1,3,4]
for i in m:
    count = 0
    for num in n:
        if i==num:
            count+=1
    print(count)'''

n =[5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
hash_list = [0]*11
for num in n:
    hash_list[num]+=1
for number in m:
    if number<1 or number>10:
        print(0)

    else:
        print(hash_list[number])