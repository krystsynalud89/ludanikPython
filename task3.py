multiples = []
array = input("Enter a numeric array and separate numbers with comma: ").split(",")
for element in array:
    if int(element) % 3 == 0:
        multiples.append(int(element))
print("Multiples of 3 in the array:", multiples)