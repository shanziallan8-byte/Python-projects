name = input("Enter student name : ")
score = int(input("Enter score (0-100): "))
if 90 <=score<= 100:
  grade = "A"
elif 80<= score <= 89:
  grad  =  "B"
elif 70<= score <=79:
  grade = "C"
elif 60<= score <= 69:
  grade = "D"
else:
    print("Fail")

print(f"\nStudent:{name} \nScore: {score}\nGrade: {grade}" )
