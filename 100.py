#this is a test. this is only a test.
print "I am a 2 number python calculator. Please enter the first whole number:"
x = int(raw_input())

print "Now enter the second whole number:"
y = int(raw_input())

print "Now tell me if you want to \n(1)add\n(2)subtract\n(3)multiply\n(4)divide"
operand = raw_input()

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y
	
def divide(x, y):
	return x / y
	
