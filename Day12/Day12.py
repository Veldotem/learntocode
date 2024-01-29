#Scope

#local scope
#within function

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
#print(potion_strength)


#Global Scope

player_health = 10

def heal():
    potion_strength = 2
    print(player_health)

heal()
print(player_health)

#block scope
if 3 > 2:
    a_variable = 10


# how to modify global scope

enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(enemies)

increase_enemies()
print(enemies)

#constants an globals

PI = 3.141592653589793
