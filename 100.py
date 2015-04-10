#this is a test. this is only a test.

prompt = '> '

print "I am a 2 number python calculator. Please enter the first whole number:"
x = int(raw_input(prompt))

print "Now enter the second whole number:"
y = int(raw_input(prompt))

print "Now tell me if you want to add, subtract, multiply, divide"
operand = raw_input(prompt)

def add(x, y):
	print "Adding"
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y
	
def divide(x, y):
	return x / y

if operand == "add":
	solution = add(x, y)
	
if operand == "subtract":
	solution = subract(x, y)
	
if operand == "multiply":
	solution = multiply(x, y)
	
if operand == "divide":
	solution = divide(x, y)
	
print solution
