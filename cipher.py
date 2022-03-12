from string import ascii_letters

def cipher(text, shift, decode=False):
    message = ''
    for i in text:
        if i not in ascii_letters:
            message += i
        else:
            message += ascii_letters[ascii_letters.index(i) - shift if decode else ascii_letters.index(i) + shift % len(ascii_letters)]

    return message



message = 'hello world'
shift = 2

print('message:', message)

encoded_message = cipher(message, shift)
print('encoded message:', encoded_message)

print('decoded_message: ', cipher(encoded_message, shift, decode=True))


