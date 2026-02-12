try:
    num=int(input("Enter the number:"))
    fact=1
    for ele in range(1,(num+1)):
        fact*=ele
    print("Factorial of number is:",fact)
except Exception as err:
    print("Error Ocurred!")
    print("Reason:",err)
print("Code execute from top to end Successfully 🥳")