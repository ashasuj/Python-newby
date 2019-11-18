#Creating F using for loop
numbers = [5, 2, 5, 2, 2]
for count in numbers:
    final_string = ""
    for j in range(count):
        final_string += "x"
    print(final_string)
