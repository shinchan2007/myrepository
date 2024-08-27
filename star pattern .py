for i in range(5):
    for j in range(3):
        if((i==0 or i==4)and j!=0):
            print("* ",end="",sep="")
        if((j==0 and i==0) or(j==0 and i==4) ):
            print(" ",end="",sep="")
        if(j==1):
            print("* ",sep="",end="")
    print()