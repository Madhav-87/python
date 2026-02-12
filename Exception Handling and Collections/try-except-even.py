try:
    num=int(input("Enter the number:"))
    if(num%2==0):
        print("The number is:",num,"even number")
    else:
        print("The number is:",num,"odd number")
except Exception:
    print("The error is:",Exception)