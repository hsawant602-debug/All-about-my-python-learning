m1 = int(input("Enter the marks of 1st subject: "))
m2 = int(input("Enter the marks of 2nd subject: "))
m3 = int(input("Enetr the marks of 3rd subject: "))
per = (m1+m2+m3)/3
if (m1 < 33) or (m2 < 33) or (m3 < 33):
    print("The student is fail because in any of the subject the marks is below 33%!")
elif per<40:
    print(f"The student is fail because the average is below 40% and the grade of the student is {per}%")
else:
    print(f"The student is passed with grade {per}%")
    