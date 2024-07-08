




























"""
while len(numbers)>1:
    p=numbers.pop(0)
    q=numbers[0]
    p1=p
    q1=q
    temp1=[]
    temp2=[]
    while p!=0:
        temp1.append(p%10)
        p=p//10
       
    print((p,p1,temp1))
    while q!=0:
        temp2.append(q%10)
        q=q//10
    
    print((q,q1,temp2))
    while len(temp1)!=0 or len(temp2)!=0:
        if temp1[-1] > temp2[-1]:
            list.append(p1)
            break
        elif temp1[-1] < temp2[-1]:
            numbers.append(p1)
            break
        else:
            temp1.pop()
            temp2.pop()
"""
