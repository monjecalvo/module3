mylist=[10,2,3,4,4,4,3,3,3,56,7]

for i in range(len(mylist)//2):
    mylist[i], mylist[len(mylist)-i-1] = mylist[len(mylist)-i-1], mylist[i]
print(mylist)    