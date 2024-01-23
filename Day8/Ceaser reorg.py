alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
charignore = [' ','!',',','.','"','§','$','%','&','/','{','(','[',')',']','=','}','?','+','*','~','#','_','-',':',';','<','>']
numbers = ['1','2','3','4','5','6','7','8','9','0']
yeno = ""
goon = True

def ceaser(direction,text,shift):
    text = text.lower()
    move = 0
    num = 0
    nprint = ""
    list = []
    # decode or encode

    if direction == "decode":
        shift *= -1

    for char in text:
        if char in charignore:
            list.append(char)
        elif char in numbers:
            num = numbers.index(char) + shift
            if num > len(numbers):
                num %= len(numbers)
            elif num < 0:
                num += len(numbers)
            list.append(numbers[num])
        elif char in alphabet:
            num = alphabet.index(char) + shift
            if num > len(alphabet):
                num %= len(alphabet)
            elif num < 0:
                num += len(alphabet)
            list.append(alphabet[num])

    nprint = ''.join(list)

    if direction == "encode":
        print(f"Your text has been encoded:\n{nprint}")

    elif direction == "decode":
        print(f"Your text has been decoded:\n{nprint}")


while goon:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
    text = input("Type in the message:\n")
    shift = int(input("Type the shift number:\n"))
    ceaser(direction,text,shift)
    yeno = input("Do you want to continue?\n")
    if yeno == "no":
        goon = False
    if goon == False:
        print("\n\nThank you for using cypher and Goodbye")
    print("\n")