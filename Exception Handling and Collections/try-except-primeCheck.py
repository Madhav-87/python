try:
    num=int(input("Enter the number:"))
    isPrime=True
    for i in range(2,(num+1)):
        if(i==num):
            continue
        if(num%i==0):
            isPrime=False
    if(isPrime):
        print("The number is prime number")
    else:
        print("The number is not prime number")
except Exception as Err:
    print("😅 Opps error occurs:")
    print("Error is:",Err)