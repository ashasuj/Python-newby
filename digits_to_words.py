# convert digits to words
number = input("Phone: ")
words = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for items in number:
    output += words.get(items, "!") + " "
print(output)
