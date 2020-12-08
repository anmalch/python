from sys import argv
from lesson_4_1 import salary

salary_script, hours, rate_per_hours, bonus = argv

print(salary(hours, rate_per_hours, bonus))
