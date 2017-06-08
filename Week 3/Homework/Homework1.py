# Exercise 1 (Complete)
# Let's look at the lowercase letters.
import string
string.ascii_lowercase

# We will consider the alphabet to be these letters, along with a space.
alphabet = string.ascii_lowercase + " "

# create `letters` here!
letters = {x: alphabet[x] for x in range(0,(len(alphabet)))}

letters


# Exercise 2 (Complete)

alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))
letters
encryption_key = 3

encoding = letters
encoding
# define `encoding` here!

for i in range(27):
    new_key = (i + encryption_key) % 27
    print(str(i) + ' - ' + str(new_key))

for i in letters:
    print(letters[i])

encoding = {alphabet[x]:(x + encryption_key) % 27 for x in range(0,(len(alphabet)))}
encoding


encoding = {letter: (place + encryption_key) % 27 for (place, letter) in enumerate(alphabet)} #answer according to text

encoding


# Exercise 3 (Complete)
message = "hi my name is caesar"

Message = list(enumerate(message))
Message

def caesar(message, encryption_key):
    # return the encoded message as a single string!
    encoding = {alphabet[x]: (x + encryption_key) % 27 for x in range(0, (len(alphabet)))}
    encodeding = ""
    for letter in message:
        # print(letters[encoding[letter]])
        # encodeding = encodeding + str(encoding[letter])
        encodeding += letters[encoding[letter]]

    return  encodeding

encoded_message = caesar(message,3)
print(encoded_message)


# Exercise 4 (Complete)
decoded_message = caesar(encoded_message,-3)
print(decoded_message)

# Testing

{x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}