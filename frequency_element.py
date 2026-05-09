'''nums = [5,8,3,1,5,2,6,6,8]          #frequency of elements in a list
freq_map = dict()
for i in range(0,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:       
        freq_map[nums[i]]=1
print(freq_map)'''


'''nums = [5,8,3,1,5,2,6,6,8]          #frequency of elements in a list using collections module
n = len(nums)
hash_map = {}
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
print(hash_map)'''