
def fizzbuzz(x):
    i = 1
    array = []
    while i < x+1:
        print(i)
        if i % 15 == 0:
            array.append("FizzBuzz")
        elif i % 3 == 0:
            array.append("Fizz")
        elif i % 5 == 0:
            array.append("Buzz")
        else:
            array.append(i)
        i += 1	
    return array

