"""
Python Basics - Quick Revision
"""

# ============================================================
# 1. VARIABLES
# ============================================================

name = "Python"
age = 30
price = 99.99
is_active = True

print(name ,"=>", type(name))
print(age,"=>" ,type(age))
print(price , " =>" , type(price))
print(is_active ,"=>" ,type(is_active))
print("_____________________________________________________________________________")
print("\n")


# Multiple assignment
x, y, z = 10, 20, 30
print(x,y,z)
# Swap variables
x, y = y, x
print("x => ", x)
print("Y =>",y)

# ============================================================
# 2. DATA TYPES
# ============================================================

integer_value = 10          # int
float_value = 10.5          # float
complex_value = 2 + 3j      # complex
string_value = "Python"     # str
boolean_value = True        # bool
none_value = None           # NoneType

print(type(integer_value))
print(complex_value , "=>" , type(complex_value))
print(boolean_value , "=>" , type(boolean_value))
print("____________________________________________")
# ============================================================
# 3. TYPE CASTING
# ============================================================

x = "100"
print(x , type(x))
int_value = int(x)
print(int_value , type(int_value))
float_value = float(x)
str_value = str(100)
print(type(str_value))
bool_value = bool(1)
print(bool_value)

# ============================================================
# 4. BASIC BUILT-IN FUNCTIONS
# ============================================================

print("Hello Python")

print(len("Python"))
type(10)
id(x)

print("_____________________________________________________")
# Useful built-ins to remember
print(abs(-10))
print(round(10.5675, 3))
print("max of (10,20,30) is = ",max(10, 20, 30) , " ; " , "using max function ex. max(10,20,30)")
print("min of (10,20,30) is = ",min(10, 20, 30) , " ; " , "using max function ex. min(10,20,30)" )
print('sum of (10,20,30)  is = ' , sum([10, 20, 30]))

print("______________________________________________________________________________________")
# ============================================================
# 5. VARIABLE NAMING
# ============================================================

user_name = "Alex"
total_amount = 500

# Constants - convention
PI = 3.14159
MAX_SIZE = 100

# ============================================================
# 6. COMMENTS
# ============================================================

# Single-line comment

"""
Multi-line string
commonly used as a docstring
"""


# ============================================================
# 7. IMPORTANT PYTHON CONCEPTS TO REMEMBER
# ============================================================

# Python is dynamically typed
value = 10
value = "Python"

# Everything in Python is an object
x = 10

# Multiple references can point to the same object
a = b = 100
print(a)
print(b)
# Python uses indentation instead of {}
