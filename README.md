# recursive-fibonacci
Recursively calculated fibonacci sequence without any recalculation

Here's the function: 
```
def fibonacci(int1, int2):
    if int1 > limit:
        print("Exceeded " + str(limit))
    else: 
        print(str(int1) + ", " + str(int2))
        temp = int1 + int2
        int1 = int2
        int2 = temp
        fibonacci(int1, int2)
```
