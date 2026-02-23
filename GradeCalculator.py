print("Enter marks for each subject (out of 100):")
marks1=float(input("Enter marks for Subject 1:"))
marks2=float(input("Enter marks for Subject 2:"))
marks3=float(input("Enter marks for Subject 3:"))
marks4=float(input("Enter marks for Subject 4:"))
marks5=float(input("Enter marks for Subject 5:"))
#Check if marks are valid
# 
if marks1 <0 or marks2 <0 or marks3<0 or marks4<0 or marks5 < 0:
    print("Error Marks cannot be negative!")

elif marks1>100 or marks2>100 or marks3>100 or marks4>100 or marks5 > 100:
     print("Error Marks cannot be greater than 100!")

else:
    #Add all marks to get total
    total_marks = marks1 + marks2 + marks3 + marks4 + marks5
    #Percentage = total / 500 * 100
    percentage = total_marks / 500 * 100

#Calculate Grade
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
     grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"


# Student passes only if ALL subjects have marks >= 40
if marks1 >= 40 and marks2 >= 40 and marks3 >= 40 and marks4 >= 40 and marks5 >= 40:
    result = "PASS"
else:
     result = "FAIL"


print("Marks Sheet")
print("Subject 1 :",marks1,"/ 100")
print("Subject 2:", marks2,"/ 100")
print("Subject 3:",marks3,"/ 100")
print("Subject 4:", marks4,"/ 100")
print("Subject 5:", marks5,"/ 100")
print("Total Marks:", total_marks,"/ 500")
print("Percentage:", percentage,"%")
print("Grade:",grade)
print("Result:",result)

