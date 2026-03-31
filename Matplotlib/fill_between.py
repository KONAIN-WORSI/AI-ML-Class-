import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ages = data['Age']
devs_salary = data['All_Devs']
py_salary = data['Python']
js_salary = data['JavaScript']

plt.plot(ages, devs_salary, linestyle = '--', label = 'Full Stack Devs')

plt.plot(ages, py_salary, label = 'Python Devs')

plt.fill_between(ages, devs_salary, py_salary, where = (py_salary > devs_salary),
                 interpolate = True, color = 'blue', alpha = 0.2, label = 'Above Full Stack Salary')

plt.fill_between(ages, devs_salary, py_salary, where = (py_salary <= devs_salary),
                 interpolate = True, color = 'red', alpha = 0.2, label = 'Below Full Stack Salary')
# plt.fill_between(ages, devs_salary, interpolate = False, color = 'Green', alpha = 0.2, label = 'Fill')

plt.legend()
plt.xlabel('Age')
plt.ylabel('Median Salary in US')
plt.title('Median salary in US by Age')
plt.tight_layout()
plt.show()