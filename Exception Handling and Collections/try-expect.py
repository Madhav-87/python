try:
    num=float(input("Enter the number:"))
    if(num%2==0):
        print("Even Number")
    else:
        print("Odd Number")
except Exception as err:
    print("Error Occured:",err)

print("Code execute from top to end Successfully 🎉")