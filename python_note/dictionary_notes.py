print("this is dictionaries")

#dictionaries let us store key:value pairs
#we use {} around dictionaries
# a dictionary saved to the variable "my_cat"
my_car = {
    "name":"toyota",
    "colour":"Blue",
    "type": "automatic"
}

# a dictionary saved to the variable "my_dog"
my_shoes = {
    "name":"Nike",
    "color":"black",
    "type":"Huarache"
}
#the keys are the first things - in this case name, breed, mood - the values are the second.

print(my_car["type"]) #selecting a value using a key instead of index

my_car["type"] = "manual" # using that method to update a value
my_car["model"]="corolla" #or creating the key if it doesn't exist yet
print(f'My dog \"{my_car["name"]}\" is a bit {my_car["type"]} none')

#dictionaries have methods just like lists. Dictionaries are muteable - they can change, so we can use methods to do that

print(my_car.keys())
#returns us a view object with all the keys in our list!

print(my_car.values())
#returns us a view object with all the values in our list!

print(my_car.items())
#returns us a view object with all the items in our list!

# the get meothd allows us to get the value of a key:
# print(my_dog.get("keygoeshere"))
# print(my_dog.get("mood"))
#we did this earlier with print(my_dog["mood"]) - so why is .get() different?

# if we start searching for a key that doesn't exist - the square brackets will give us an error and stop our code!
# the .get() method will return us the blank data type "None"

print(my_car.get("wheels")) #<- this will work!
# print(my_dog["legs"]) <- this will not!

#we can also give a second arguement to get - a customer error message / bit of data rather than "none"
print(my_car.get("wheels","This key does not exist")) #<- this will work!

#we can use the .update() method to add or update keys and values in our list!
my_car.update({"wheels":"4"})
my_car.update({"name":"Benz"})
print(my_car)

#and .pop() to remove keys - and their values will go too
my_car.pop("type")
print(my_car)

#viewing a dictionary isn't the nicest in a terminal!

print(my_car.keys()) #prints it normally - as a "view object"
print(list(my_car.keys())) #converts the view object to a list!

# or we could use a handy for loop - because this is iterable!
for every_key in my_car.keys():
    print(every_key)