# emoji convertor using function
# emoji converter
message = input("> ")


def convert(input):
    word_list = message.split(' ')

    emojis = {
        ":)": "😊",
        ":(": "😒"
    }

    output = ""
    for word in word_list:
        output += emojis.get(word, word) + " "
    return (output)


print(convert(message))
