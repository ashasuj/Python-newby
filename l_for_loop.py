#Writing L using for loop
numbers = [2, 2, 2, 2, 2,6]
for count in numbers:
    final_string = ""
    for j in range(count):
        final_string  += "x"
    print(final_string)
