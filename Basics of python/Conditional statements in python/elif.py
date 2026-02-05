#Code for demonstrating the elif statement in python.
marks=int(input("Enter your marks:"))
if marks<=100 and marks>=95:
    print("Grade:O")
elif marks<95 and marks>=90:
    print("Grade:A+")
elif marks>=85 and marks<90:
    print("Grade:A")
elif marks>=80 and marks<85:
    print("Grade:B+")
elif marks>=75 and marks<80:
    print("Grade:B")
elif marks>=70 and marks<75:
    print("Grade:C")
else:
    print("Less than 65 marks")