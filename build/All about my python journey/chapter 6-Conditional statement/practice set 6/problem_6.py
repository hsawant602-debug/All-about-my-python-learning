marks = int(input("Enter the marks: "))

if(90<=marks and marks<=100):
    print("Excellent!")
elif(80<marks and marks<=90):
    print("Grade A")
elif(70<marks and marks<=80):
    print("Grade B")
elif(60<marks and marks<=70):
    print("Grade C")
elif(50<marks and marks<=60):
    print("Grade D")
else:
    print("Fail")