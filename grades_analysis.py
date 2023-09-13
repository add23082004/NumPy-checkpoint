# Import the numpy library
import numpy as np

# Create the "grades" array as specified above.
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
print("Here is the grades array:", grades)

# Use numpy functions to calculate the mean, median, and standard deviation of the grades.
mean = np.mean(grades)
median = np.median(grades)
standard_deviation = np.std(grades)
print("The mean, median, and standard deviation of the grades are respectively:", mean, median, standard_deviation)

# Use numpy function to find the maximum and minimum of the grades.
max_grades = np.max(grades)
min_grades = np.min(grades)
print("The maximum and minimum of the grades are respectively:", max_grades, min_grades)

# Use numpy function to sort the grades in ascending order.
print("Here are the grades sorted in ascending order:", np.sort(grades))

# Use numpy function to find the index of the highest grade in the array.
highest_grade_index = np.argmax(grades)
print("Here is the index of the highest grade in the array:", highest_grade_index)

# Use numpy function to count the number of students who scored above 90.
number_of_students_who_scored_above_90 = np.count_nonzero(grades > 90)
print("There are", number_of_students_who_scored_above_90, "students who scored above 90.")

# Use numpy function to calculate the percentage of students who scored above 90.
percentage_of_students_who_scored_above_90 = np.mean(grades > 90) * 100
print("Here is the percentage of students who scored above 90:", percentage_of_students_who_scored_above_90)

# Use numpy function to calculate the percentage of students who scored below 75.
percentage_of_students_who_scored_below_75 = np.mean(grades < 75) * 100
print("Here is the percentage of students who scored below 75:", percentage_of_students_who_scored_below_75)


# Use numpy function to extract all the grades above 90 and put them in a new array called "high_performers".
high_performers = grades[grades > 90]
print("Here is the high performers array:", high_performers)

# Create a new array called "passing_grades" that contains all the grades above 75.
passing_grades = grades[grades > 75]
print("Here is the medium performers array:", passing_grades)
