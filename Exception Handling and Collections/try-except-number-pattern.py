try:
    #Code for generating the following pattern:
    '''
    1
    12
    123
    1234
    '''
    #-------------------------------#

    #-To decide number of columns-#
    col=4
    #-To decide number of rows-#
    row=1
    #-To specify the value-#
    num=1

    #-------------------------------#
    for ele in range(1,col+1):
        for i in range(1,row+1):
            print(num,end="")
            num+=1
        row+=1
        num=1
        print("\n")
    #-------------------------------#
except Exception as err:
    print("😅 Oops Error ocurred!")
    print("The Error is:",err)