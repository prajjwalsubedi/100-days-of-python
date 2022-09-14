alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

status = "yes"
while status == "yes" or status == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #code
    text_list = list(text)
    final = ""

    def edcode():
        for number in range(len(text_list)):
            index = text_list[number]
            if index in alphabet:
                alphabet_index = alphabet.index(index)
                if direction == "encode":
                    change_number = alphabet_index + shift
                elif direction == "decode":
                    change_number = alphabet_index - shift
                else:
                    print("Please enter valid details.!!!")
                if change_number > 25:
                    change_number = change_number - 26
                text_list[number] = alphabet[change_number]

        final = "".join(text_list)
        print(final)

    edcode()
    status = input("Do you want to run this program again?? type yes or no:  ")
if status != "yes" or status != "y":
    print("Thank you for using this code..")
