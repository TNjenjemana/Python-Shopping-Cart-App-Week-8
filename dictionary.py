#dictionary is a collection of key value pairs,unlike lists or tuples which are indexed by a range of numbers
# dictionaries are indexed by keys which can be of any type. it can be a string or numeric data type
# dictionaries are mutable/changable
# Define a dictionary by using curley braces, and key value pairs separated by a colon
my_dict = {'apple':3,'banana':5,'orange':2} #apple,banana etc are keys, 3,5,2 are corresponding values

print(my_dict['banana']) #number associated with a key is accessed by using square braces

my_dict['grapes'] = 4 #add another item to existing dictionary
print(my_dict)

my_dict['banana'] = 7 #changing the value of banana from 5 to7. modifying an existing value
print(my_dict)