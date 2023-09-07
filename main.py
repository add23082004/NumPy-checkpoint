import numpy as np

grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
print(grades)

print(np.mean(grades))
print(np.median(grades))
print(np.std(grades))

print(np.max(grades))
print(np.min(grades))

print(np.sort(grades))

print(np.argmax(grades))

print(np.count_nonzero(grades > 90))

print(np.mean(grades > 90) * 100)

print(np.mean(grades < 75) * 100)

high_performers = grades[grades > 90]
print(high_performers)

passing_grades = grades[grades > 75]
print(passing_grades)
