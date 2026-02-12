try:
        # Code for generating this patter:
    '''
    *
    * *
    * * *
    '''
    #code for it:
    row=3
    col=1
    for i in range(1,row+1):
        for ele in range(1,col+1):
            if(ele>col):
                break
            print("*",end=" ")
        col+=1
        print("\n")
except Exception as err:
    print("😅 Oops Error ocurred!")
    print("The Error is:",err)
    