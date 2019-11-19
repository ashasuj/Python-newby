# Program to remove duplicates in a list

numbers = [55, 55, 55,666,44,44,44]
no_duplicates =[]

for item in numbers:
    if item not in no_duplicates:
        no_duplicates.append(item)
print(no_duplicates)
