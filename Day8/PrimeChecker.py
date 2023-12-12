
def prime_checker(number):
    if number <= 1:
        return (False)
    for i in range(2, number-1):
        print(i)
        if number % i == 0:
            return False
    return (True)

n=int(input("Enter a number between 1 and 100:"))

if prime_checker(number=n):
    print("is Prime!")
else:
    print("Not a Prime!")