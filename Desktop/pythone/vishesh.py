# 1
marks = {'Maths': [78, 89, 95, 65, 88, 92, 76, 84, 80, 90], 
         'Science': [85, 90, 78, 88, 92, 75, 80, 85, 94, 86], 
         'English': [80, 85, 92, 88, 75, 90, 95, 78, 84, 82], 
         'IT': [88, 94, 80, 78, 85, 90, 92, 88, 76, 84]}
for subject, scores in marks.items():
    print(f'{subject}: Highest={max(scores)}, Lowest={min(scores)}, Average={sum(scores)/len(scores)}')
overall = [sum(x) for x in zip(*marks.values())]
print(f'Overall: Highest={max(overall)}, Lowest={min(overall)}, Average={sum(overall)/len(overall)}')

# 2



basic_salary = float(input("Enter Basic Salary: "))
if basic_salary <= 10000:
    hra = 0.2 * basic_salary
    da = 0.8 * basic_salary
elif basic_salary <= 20000:
    hra = 0.25 * basic_salary
    da = 0.9 * basic_salary
else:
    hra = 0.3 * basic_salary
    da = 0.95 * basic_salary
gross_salary = basic_salary + hra + da
print(f"Gross Salary: {gross_salary}")

# 3


import re
password = input("Enter Password: ")
if (re.search('[a-z]', password) and re.search('[A-Z]', password) and 
    re.search('[0-9]', password) and re.search('[@#$]', password) and 
    6 <= len(password) <= 16):
    print("Password is valid")
else:
    print("Password is invalid")

# 4



L = [10, 20, 30, 40, 50, 60, 70, 80]
L.append(200)
L.append(300)
print(L)
L = [x for x in L if x != 10 and x != 30]
print(L)
print(sorted(L))
print(sorted(L, reverse=True))

# 5


D = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
D[6] = "Six"
print(D)
D.pop(2, None)
print(D)
print(6 in D)
print(len(D))
print(sum(D.keys()))

# 6
import random
numbers = [random.randint(100, 900) for _ in range(100)]
odd = [x for x in numbers if x % 2 != 0]
even = [x for x in numbers if x % 2 == 0]
prime = [x for x in numbers if all(x % i != 0 for i in range(2, int(x**0.5)+1))]
print(len(odd), len(even), len(prime))

# 7
def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time)
p, r, t = 10000, 5, 2
print(compound_interest(p, r, t))

# 8A
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}, Cuisine Type: {self.cuisine_type}")
    def open_restaurant(self):
        print("The restaurant is open.")
restaurant = Restaurant("Tasty Bites", "Indian")
print(restaurant.restaurant_name, restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 8B
class User:
    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.profile = kwargs
    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Profile: {self.profile}")
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")
user1 = User("John", "Doe", age=30, location="NY")
user2 = User("Jane", "Smith", age=25, location="LA")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
