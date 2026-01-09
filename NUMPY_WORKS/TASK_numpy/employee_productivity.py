import numpy as np


productivity = np.array([
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])

#1. Calculate the total number of hours worked by each employee over 10 days.
print(np.sum(productivity,axis=0))
#2. Calculate the total work hours for each day across all employees.
print(np.sum(productivity,axis=1))
#3. Find the average working hours per employee.
print(np.average(productivity,axis=1))
#4. Find the average working hours per day.
print(np.average(productivity,axis=0))

#5. Identify the employee index who worked the maximum total hours.
employee_wise_total=np.sum(productivity,axis=1)
print(employee_wise_total)


print(np.argmax(employee_wise_total))
#6. Identify the employee index who worked the minimum total hours.
print(np.argmin(employee_wise_total))
#7. Find the day index with the highest total working hours.
day_wise_total=np.sum(productivity,axis=0)
print(day_wise_total)
print(np.argmax(day_wise_total))
#8. Identify employees who are overworked if average hours exceed 8 per day.
avg_hr=np.average(productivity,axis=1)
print(avg_hr)
print(np.argmax(avg_hr))
#9. Calculate the difference between the most productive and least
difference=np.max(avg_hr)-np.min(avg_hr)
print(difference)