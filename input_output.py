# ==========================================
# 02_input_output.py
# ==========================================


# 1. print() with sep
print("using of sep= ' ' ")
print("2026", "08", "15", sep="-")
print("Python", "Revision", sep=" | ")
print("shivam" , "gaiwkad" , sep="_")

# 3. print() with end
print("Hello", end=" ")
print("World")

print("One", end=" -> ")
print("Two")




#  input()
name = input("Enter your name: ")
print("Hello", name)


# 7. input() is always string
age = int(input("Enter your age: "))

print(type(age))


# 8. Type conversion
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print(age)
print(height)


# 9. Multiple inputs
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print(first_name, last_name)


# 10. f-string
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")


# 11. Basic input/output program
name = input("Enter your name: ")
city = input("Enter your city: ")

print(f"Name: {name}")
print(f"City: {city}")

