def greet(name):
    print(f"Hello {name}")
    print("How are you?")
    print("Isn't the weather nice today")

name = "Finn"
location = "San Francisco"
greet(name)



def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(name, location)
