# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
number_of_students = 0
sum_of_heights = 0
for n in student_heights:
	sum_of_heights += n
	number_of_students += 1

avg_height = round(sum_of_heights / number_of_students)

print(avg_height)
