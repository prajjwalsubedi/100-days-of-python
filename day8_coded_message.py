alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#code
text_list = list(text)
final = ""


def encode():
	for number in range(len(text_list)):
		index = text_list[number]
		alphabet_index = alphabet.index(index)
		change_number = alphabet_index + shift
		if change_number > 25:
			change_number = change_number - 26
		text_list[number] = alphabet[change_number]

	final = "".join(text_list)
	print(final)


#print(text_list)
def decode():
	for number in range(len(text_list)):
		index = text_list[number]
		alphabet_index = alphabet.index(index)
		change_number = alphabet_index - shift
		if change_number > 25:
			change_number = change_number - 26
		text_list[number] = alphabet[change_number]

	final = "".join(text_list)
	print(final)


if direction == "encode":
	encode()
elif direction == "decode":
	decode()
else:
	print("Please enter valid details.!!!")
