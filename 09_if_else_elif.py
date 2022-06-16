name = input("Enter you child's name? ")
age = int(input("Enter you child's age? "))
age_at_school = 5

if (age==age_at_school):
    print("Congratulation! ",name," can go to school.")
elif (age>age_at_school):
    print('You are too late! Be Hurry to get him admitted')
else: 
    print(name," can not go to school.")