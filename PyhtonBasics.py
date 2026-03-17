"""
PYTHON BASICS REVISION SCRIPT
Run this file to quickly revise core Python concepts.
"""

# -----------------------------
# 1. VARIABLES & DATA TYPES
# -----------------------------
print("\n--- 1. VARIABLES & DATA TYPES ---")

name = "Samad"
age = 20
height = 5.9
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

print("Type of name:", type(name))
print("Type of age:", type(age))


# -----------------------------
# 2. OPERATORS
# -----------------------------
print("\n--- 2. OPERATORS ---")

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Power:", a ** b)
print("Modulus:", a % b)


# -----------------------------
# 3. CONDITIONAL STATEMENTS
# -----------------------------
print("\n--- 3. IF / ELSE ---")

number = 7

if number > 10:
    print("Number is greater than 10")
elif number == 10:
    print("Number is exactly 10")
else:
    print("Number is less than 10")


# -----------------------------
# 4. LOOPS
# -----------------------------
print("\n--- 4. LOOPS ---")

print("For loop:")
for i in range(5):
    print(i)

print("While loop:")
count = 0
while count < 3:
    print("Count:", count)
    count += 1


# -----------------------------
# 5. LISTS
# -----------------------------
print("\n--- 5. LISTS ---")

numbers = [1, 2, 3, 4, 5]

numbers.append(6)
numbers.remove(2)

print("List:", numbers)

for num in numbers:
    print("Element:", num)


# -----------------------------
# 6. TUPLES
# -----------------------------
print("\n--- 6. TUPLES ---")

coordinates = (10, 20)

print("Tuple:", coordinates)
print("First element:", coordinates[0])


# -----------------------------
# 7. SETS
# -----------------------------
print("\n--- 7. SETS ---")

unique_numbers = {1, 2, 3, 3, 4}

unique_numbers.add(5)

print("Set:", unique_numbers)


# -----------------------------
# 8. DICTIONARIES
# -----------------------------
print("\n--- 8. DICTIONARIES ---")

student = {
    "name": "Samad",
    "age": 20,
    "course": "Software Engineering"
}

print("Student name:", student["name"])

student["age"] = 21

for key, value in student.items():
    print(key, ":", value)


# -----------------------------
# 9. FUNCTIONS
# -----------------------------
print("\n--- 9. FUNCTIONS ---")

def greet(name):
    return f"Hello {name}"

print(greet("Samad"))


def add(x, y):
    return x + y

print("Sum:", add(5, 6))


# -----------------------------
# 10. LAMBDA FUNCTIONS
# -----------------------------
print("\n--- 10. LAMBDA ---")

square = lambda x: x * x
print("Square:", square(5))


# -----------------------------
# 11. LIST COMPREHENSION
# -----------------------------
print("\n--- 11. LIST COMPREHENSION ---")

squares = [x**2 for x in range(6)]
print("Squares:", squares)


# -----------------------------
# 12. EXCEPTION HANDLING
# -----------------------------
print("\n--- 12. EXCEPTION HANDLING ---")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    print("Execution finished")


# -----------------------------
# 13. OBJECT ORIENTED PROGRAMMING
# -----------------------------
print("\n--- 13. OOP ---")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")


p1 = Person("Samad", 20)
p1.introduce()


# -----------------------------
# 14. FILE HANDLING
# -----------------------------
print("\n--- 14. FILE HANDLING ---")

with open("sample.txt", "w") as file:
    file.write("Hello Python\n")

with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:", content)


# -----------------------------
# 15. MODULE IMPORT
# -----------------------------
print("\n--- 15. MODULES ---")

import math
import random

print("Square root of 16:", math.sqrt(16))
print("Random number:", random.randint(1, 10))


# -----------------------------
# END
# -----------------------------
print("\nPython basics revision completed!")
