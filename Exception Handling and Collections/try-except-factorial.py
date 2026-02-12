try:
    fact=1
    num=int(input("Enter the number:"))
    for ele in range(1,(num+1)):
        fact*=ele
    print("The factorial of number is:",fact)
except:
    print("😅 Error in code:")
    print("The Error is like :",Exception)


