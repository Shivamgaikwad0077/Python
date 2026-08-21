print("Types of oprators in python  : ")
print(""" 
Types of operators in python 
        │
        ├── 1. Arithmetic operators
        ├── 2. Comparison operators
        ├── 3. Assignment operators
        ├── 4. Logical operators
        ├── 5. Identity operators
        ├── 6. Membership operators
        └── 7. Bitwise operators
""")
print("___________________________________________________________")
print("1. Arithmetic oprators :  + , - , * , / , // , % , ** : ")
a = 10
b = 20 
print("a + b = " , a+b)
print("a - b =", a-b)
print("a * b =" , a*b)
print("a / b = ", a/b)
print("a // b = ", a//b)
print("a % b = ", a%b)
print("a ** b = ", a**b)

print("___________________________________________________________")
print("2. Comparison oprators :  == , != , > , < , >= , <= : ")
print(f"{a} == {b} ", "=" ,a==b)
print(f"{a} != {b} ", "=" ,a !=b)
print(f"{a} > {b} ", "=" ,a > b)
print(f"{a} < {b} ", "=" ,a < b)
print(f"{a} >= {b} ", "=" ,a >= b)
print(f"{a} <= {b} ", "=" ,a <= b)

print("___________________________________________________________")
print("3. Assignments oprators :  += , -= , *= , /= , //= , *= , **= , &=, ^= , <<= , >>= : ")


s = 5
s **= 5
print(f"{s} **=5 " , "=" , s) 

x = 10
x += 5
print('x += 5 ', "=" , x)

x -= 5
print("x -= 5" , "=" , x)

x *= 5
print("x *= 5" , "=" , x)


x /= 5
print("x /= 5" , "=" , x)

x //= 5
print("x //= 5" , "=" , x)

print("___________________________________________________________")
print("4. logical oprators : ")

n = 10
print( f" '({n} > 5 and {n} < 20)' " , "=" ,n > 5 and n < 20)

print( f" '({n} > 5 or {n} < 20)' " , "=" ,n > 5 or n < 20)

print(f"'(not {n} > 5)'", "=", not n > 5)

print("___________________________________________________________")
print("5 : Membership oprators  : in , not in ")

fruits = ['apple' , "banana" , "mango"]
print("apple" in fruits)
print("orange" in fruits)
print("orange" not in fruits)
print("apple" not in fruits)

name = "Python"

print("P" in name)
print("z" in name)
print("z" not in name)

print("___________________________________________________________")
print("6 : identity oprators  : is , is not ")

a = [10,20,30]
b = a
c = [34,55,22]
print(a is b) #it will return true 
print(a is not b)# it wil return false
print(a is c )#it will return falase
print(b is a) # it will return true beacuse a is in b
