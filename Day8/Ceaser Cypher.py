alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
text = input("Type in the message:\n")
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    text = text.lower()
    list = []
    for char in text:
        list.append(alphabet[alphabet.index(char)+shift])
    print("".join(list))

encrypt(text,shift)
