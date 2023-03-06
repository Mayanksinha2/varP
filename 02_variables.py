# variables
var1 = "Manku"
var2 = "Hello..!!"
var3 = "45"
var4 = 34.5
var5 = "65"
var6 = 35
print(type(var1))
print(var2)
print(var6)
print(var3 + var5)
print(5*(var6))
print(5*(var5))

# TypeCasting
""" 
we can use -
int()
float()
str()
for typecasting....
"""

print(int(var3) + int(var5))


# For taking an input from an user ...

print("Enter your number") # The number we are taking as a input will be print as a string .
inpnum = input()
print("Your number is", inpnum)
print("Your input", int(inpnum)+10)


# Calculator for two numbers by taking inputs from the user

print("Enter your first no:")
num1 = input()
print("Enter your second no:")
num2 = input()
print("Your required result is:",int(num1)+int(num2))
print("Your required result is:",int(num1)-int(num2))
print("Your required result is:",int(num1)*int(num2))
print("Your required result is:",int(num1)/int(num2))