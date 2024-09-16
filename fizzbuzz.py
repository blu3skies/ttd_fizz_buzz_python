
def fizzbuzz(x):
    i = 1
    array = []
    while i < x+1:
        print(i)
        if i % 15 == 0:
            array.append("FizzBuzz")
            i += 1	
        elif i % 3 == 0:
            array.append("Fizz")
            #print(array)
            i += 1	
        elif i % 5 == 0:
            array.append("Buzz")
            #print(array)
            i += 1	
        else:
            array.append(i)
            #print(array)
            i += 1	
        #print(array)
    return array

