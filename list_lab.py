"""
#SERIES 1
fruits = ["apple", "pear", "orange", "peach"]
print (fruits)
new_fruit = input("What fruit should be added to the list?\n")
fruits.append(new_fruit)
print (fruits)
fruit_number = int(input("Give me a number and I'll tell you which fruit it corresponds to.\n"))
print ("Fruit number", fruit_number, "is the", fruits[fruit_number-1])
fruits += ["Evanberries"]
print (fruits)
fruits.insert(0, "Jadeberry")
print (fruits)
for i in fruits:
    if i.startswith("p"):
        print (i)


#SERIES 2
fruits = ["apple", "pear", "orange", "peach"]
print (fruits)
fruits.pop(-1)
print (fruits)
fruit_to_delete = input("Which fruit of the above fruits should be removed?")
fruits.remove(fruit_to_delete)
print (fruits)
"""
"""
#SERIES 3
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
copy_fruits = []
apple = input ("do you like apples?")
if apple == "yes":
    copy_fruits.append(fruits[0])

while apple != "yes" or "no":
    apple = input ("Please answer yes or no if you like apples")
    if apple == "yes":
        copy_fruits.append(fruits[0])
        
"""


#SERIES 4   #Make a new list with the contents of the original, but with all the letters in each item reversed.
fruits = ["apple", "pear", "orange", "peach", "Ken Patner", "BJ Albornoz"]
new_fruits = []  
for i in fruits:
    new_fruits.append(i[::-1])
    print (new_fruits)