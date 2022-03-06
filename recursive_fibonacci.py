# Test if limit input is a valid integer
while True:
    try:
        limit = int(input("How high? ")) 
    except ValueError:
        print("Sorry, I need an integer.")
        continue
    if limit <= 0:
        print("Sorry your input must be greater than 0.")
        continue
    else:
        break

# Fibonacci function without recalculation
def fibonacci(int1, int2):
    if int1 > limit:
        print("Exceeded " + str(limit))
    else: 
        print(str(int1) + ", " + str(int2))
        temp = int1 + int2
        int1 = int2
        int2 = temp
        fibonacci(int1, int2)

# Function call     
fibonacci(0, 1)