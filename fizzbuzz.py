
def fizzbuzz(x):
    i = 1
    array = []
    while i < x+1:
        if i % 3 == 0:
            array.append("Fizz")
            # print(array)
            i += 1	
        else:
            array.append(i)
            # print(array)
        i += 1	
    return array
