# emoji converter
message = input("> ")
word_list = message.split(' ')

emojis = {
    ":)": "😊",
    ":(": "😒"
}
output = ""
for word in word_list:
    output += emojis.get(word, word) + " "
print(output)