alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
charignore = [' ','!',',','.','"','§','$','%','&','/','{','(','[',')',']','=','}','?','+','*','~','#','_','-',':',';','<','>']
numbers = ['1','2','3','4','5','6','7','8','9','0']
direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
text = input("Type in the message:\n")
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift,):
    text = text.lower()
    list = []
    num = 0
    for char in text:
        if char in charignore:
            list.append(char)
        elif char in numbers:
            num = numbers.index(char) + shift
            if num > len(numbers):
                num %= len(numbers)
            list.append(numbers[num])
        elif char in alphabet:
            num = alphabet.index(char) + shift
            if num > len(alphabet):
                num %= len(alphabet)
            list.append(alphabet[num])
    print(''.join(list))

def decrypt(text, shift,):
    text = text.lower()
    list = []
    num = 0
    for char in text:
        if char in charignore:
            list.append(char)
        elif char in numbers:
            num = numbers.index(char) - shift
            if num < 0:
                num += len(numbers)
            list.append(numbers[num])
        elif char in alphabet:
            num = alphabet.index(char) - shift
            if num < 0:
                num += len(alphabet)
            list.append(alphabet[num])
    print(''.join(list))


if direction == "encrypt":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
