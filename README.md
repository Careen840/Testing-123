# FIZZBUZZ Question
for x in range(1, 100):
    if (x % 3==0) and (x % 5==0):
        print("FizzBuzz")
    elif x % 3== 0:
        print("Fizz")
    elif x % 5==0 :
        print("Buzz")
    else:
        print(x)
        
        
###second solution
        
def input(i):
    if (i% 3==0) and (i% 5==0):
        return "FizzBuzz"
    elif i % 3== 0:
        return"Fizz"
    elif i % 5==0 :
        return"Buzz"
    return i
print (input(27))
