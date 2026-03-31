import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

department = ['Computer Science', 'Mathematics', 'Physics', 'Chemistry',
              'Aerospace', 'Biology', 'History', 'Geography']

no_of_students = [120, 80, 70, 36, 89, 45, 60, 20]

plt.barh(department, no_of_students, edgecolor = 'black')

for i, value in enumerate(no_of_students):
    plt.text(i, value + 1, value, ha = 'center')


plt.xlabel('Departments')
plt.ylabel('No of Students')
plt.title('Number of Students in each Department')
plt.show()