A=int(input())
B=int(input())
for num in range(A,B+1):
    flag = False
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                flag=True
                break
    if flag:
        print(num,"is Composite Number")
    else:
        if num>0:
            if num==1:
                print(num,"Neither Prime Nor Composite")
            else:
                print(num,"is Prime Number")
        else:
            print("Invalid Input")
            break