print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=90 :
    print("Your Grade is A+")
elif avg>=80 and avg<89:
    print("Your Grade is A")
elif avg>=70 and avg<79:
    print("Your Grade is B")
elif avg>=60 and avg<69:
    print("Your Grade is C")
elif avg>=50 and avg<59:
    print("Your Grade is D")
elif avg< 50  :
    print("Your Grade is fail")
else:
    print("Invalid Input!")
