from ceasar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def ceasar(message, shift_num, direction):
    output = ""
    type = ""
    shifted_possition = 0
    
    for letter in message:
        if letter not in alphabet:
            output += letter
        else:
            if direction == "encode":
                shifted_possition = alphabet.index(letter) + shift_num
                type = "encoded"
            elif direction == "decode":
                shifted_possition = alphabet.index(letter) - shift_num
                type = "decoded"
            else:
                print("This not an valid choice.")
            shifted_possition %= len(alphabet) # always gives number 0 - 25
            output += alphabet[shifted_possition]
        
    print(f"Here is the {type} result: {output}")
    
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type your sift number: "))

    ceasar(text, shift, direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")