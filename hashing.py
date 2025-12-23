num=[5,9,8,6,4,6,2,4,5,5,4,6,4,10,2,5]
m=[2,5,6,56,986,12,25,65,8,5,4,8,5,5,]
hash_dict={}
for i in num: #o(n)
    if num[i] in hash_dict:
        hash_dict[num[i]]+=1 # o(1)
    else:
        hash_dict[num[i]]=1 #o(1)
print(hash_dict)
for x in range(0,len(m)):
    if m[x] in hash_dict:
        print(hash_dict[num[i]])
    else:
        print(0)
