#Dictionaries
dictionary = {
    "Bug" : "an Error in a Program",
    "Code" : "Instructions for a computer to run",
    "Loop" : "The action of doing something over and over again"
}

print(dictionary["Bug"])

#Nesting

capitals = {
    "Francce" : "Paris",
    "Germany" : "Berlin",
    "United Kingdom" : "London"
}

travel_log ={
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"]
}

travel_log_exp ={
    "France" : {cities_visited : ["Paris", "Lille", "Dijon"]},
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"]}