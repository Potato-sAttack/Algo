p=9
list=[]
while p!=0:
    list.append(p%10)
    p=p//10
list.reverse()
print(list)