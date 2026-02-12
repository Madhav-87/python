try:
    num=[1,2,3,4,5,6]
    print("The reverse of number is:")
    num.reverse()
    for i in range(0,len(num)):
        print(num[i],end=" ")
except Exception as Err:
    print("Oops the error ocurrs")
    print("The error is:",Err)
