
#a list is a built that holds a collection of items.these items can be various types such as intigers,strings and even other lists
#lists are ordered and changable and allow for duplicates
fruits = ["apple","banana","cherry"]
#python list are zero indexed, meaning first item is at zero index, then second is at 1

print(fruits[2]) # using index number of item

fruits[0] = "blueberry" #interchange items
print(fruits)

fruits = ["apple","banana","cherry"]

fruits.append("kiwi") #adding items to a list
print(fruits)

fruits.insert(2,"orange") # inserting an item anywhere in the list
print(fruits)

fruits.remove("kiwi") #remove method removes 1 item if that item is repeated in the list
print(fruits)

fruits.sort(reverse=True) #for normal foward sort use()only, but if you want the list in reverse order in brackets write (reverse= true)
print(fruits)

