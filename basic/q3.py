grades = ["A","B","C","D","F"]

score = int(input("enter your score: "))
if(score > 100):
    print("invalid score")
    exit()
elif(score >= 90):
    print(grades[0])
elif (score >= 80 and score < 90):
    print(grades[1])
elif (score >= 70 and score < 80):
    print(grades[2])
elif (score >= 60 and score < 70):
    print(grades[3])
elif (score < 60):
    print(grades[4])
