try:
    # Getting the number from the user
    limitEnd=int(input("Enter the number:"))
    num=0
    num2=1
    print("The Fibonacci series is:")
    print(num)
    print(num2)

    # Getting the loop for printing the fibonacci series
    
    for ele in range(0,(limitEnd+1)):
        ans=num+num2
        if(ans>limitEnd):
            break
        print(ans)
        num=num2
        num2=ans
except Exception as Err:
    print("😅 Opps error occurs:")
    print("Error is:",Err)
