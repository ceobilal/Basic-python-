# arthmatic operators
a = 10
b = 3
print("Addition:", a + b)         # 13
print("Subtraction:", a - b)      # 7
print("Multiplication:", a * b)   # 30
print("Division:", a / b)         # 3.333...
print("Floor Division:", a // b)  # 3
print("Modulus:", a % b)          # 1
print("Power:", a ** b)           # 1000

# exmple 
c=a+b     # hear example  ,a-b,a*b,a/b,a//b,a%b,a**b  
print(c)
# example 
print(a+b) # print(a-b) , print(a*b) , print(a/b) , print(a//b) , print(a%b) , print(a**b)  
c=a+b
print(c)

# Assigment Operators




#(Simple Assignment)
x = 5
print(x)      # Output: 5
#(Add and Assign)
x = 5
x += 3        # x = x + 3
print(x)      # Output: 8

#(Subtract and Assign)
x = 5
x -= 3        # x = x - 3
print(x)      # Output: 2

#(Multiply and Assign)
x = 5
x *= 3        # x = x * 3
print(x)      # Output: 15

#(Divide and Assign)
x = 9
x /= 3        # x = x / 3
print(x)      # Output: 3.0


#(Modulus and Assign)
x = 10
x %= 3        # x = x % 3
print(x)      # Output: 1

# (Floor Divide and Assign)
x = 10
x //= 3       # x = x // 3
print(x)      # Output: 3

#(Power and Assign)
x = 2
x **= 3       # x = x ** 3
print(x)      # Output: 8


#Python Comparison Operators



#Equal)
x = 5
y = 5
print(x == y)   # True (because 5 is equal to 5)

#(Not Equal)
x = 5
y = 3
print(x != y)   # True (because 5 is not equal to 3)

#(Greater Than)
x = 7
y = 4
print(x > y)    # True (7 is greater than 4)

#(Less Than)
x = 2
y = 6
print(x < y)    # True (2 is less than 6)

# (Greater Than or Equal To)
x = 5
y = 5
print(x >= y)   # True (5 is equal to 5)

#(Less Than or Equal To)
x = 3
y = 5
print(x <= y)   # True (3 is less than 5)



# Python Logical Operators



# and — Both conditions must be true
x = 7
print(x > 5 and x < 10)  # True because 7 > 5 AND 7 < 10

#or Operator
x = 3
print(x < 5 or x > 10)  # True because 3 < 5 (even though 3 is not > 10)

#not Operator
x = 7
print(not (x < 5 and x < 10))  # not (False and True) → not False → True

