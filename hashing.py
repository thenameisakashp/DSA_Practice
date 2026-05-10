'''n = [5,8,3,1,5,2,6,6,8]    #hashing technique to count the frequency of elements in a list
m = [10,5,6,8,9,2,1,3,4]
for i in m:
    count = 0
    for num in n:
        if i==num:
            count+=1
    print(count)'''

'''n =[5,3,2,2,1,5,5,7,5,10]     #hashing optimal way to count the frequency of elements in a list
m = [10,111,1,9,5,67,2]
hash_list = [0]*11
for num in n:
    hash_list[num]+=1
for number in m:
    if number<1 or number>10:
        print(0)
    else:
        print(hash_list[number])'''

'''n =[5,3,2,2,1,5,5,7,5,10]     #hashing optimal way to count the frequency of elements in a list using dictionary
m = [10,111,1,9,5,67,2]
num = len(n)
hash_list = dict()  
for i in range(0,num):
    hash_list[n[i]] = hash_list.get(n[i],0)+1
for number in m:
    if number<1 or number>10:
        print(0)
    else:
        print(hash_list.get(number,0))'''