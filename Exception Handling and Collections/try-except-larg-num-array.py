try:
    array=[1,2,3,4,5,6,7,8,9]
    array.sort()
    largestNum=array[0]
    for ele in range(0,len(array)):
        if(largestNum<array[ele]):
            largestNum=array[ele]
    print("The largest number is:",largestNum)
except Exception as err:
    print("😅 Oops Error ocurred!")
    print("The Error is:",err)