# ask the user to put two number
num1, num2 = input("ENTER TO NUMBERS:").split()

# define the number as integer
num1 = int(num1)
num2 = int(num2)

# additiion of two numbers
addition = num1 + num2

# mini of two numbers
difference = num1 - num2

# mutilply of two numbers
product = num1 * num2

# divide  of two numbers
quotient = num1 / num2

# reminder of two numbers
reminder = num1 % num2

print("{} + {} = {}".format(num1, num2, addition))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, reminder))