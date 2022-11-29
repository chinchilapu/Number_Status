A=int(input("Enter the smallest value of the range: "))
B=int(input("Enter the largest value of the range: "))
print("In the range of ["+str(A)+","+str(B)+"]")
for i in range(A,B+1):
        if i==1:
            print(i,"is neither Prime nor Composite")
        num=2
        for j in range(2,i//2+1):
            if (i%j==0):
                num=1
                break
        if (num==2):
            print(i,"is a Prime number")
        else:
            print(i,"is a Composite number")