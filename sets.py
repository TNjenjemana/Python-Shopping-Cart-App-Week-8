
# a set in python is an unordered collection of unique elements 
# sets do not allow duplicate values. usefull when perfoming operations like union, intersection and a difference between a colloction of elements
#sets are unordered and immutable, but can add and remove

my_set = {1,2,3,4,5} # sets use curley brackets
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

#operations and sets - sets supports variuos operations which allow you to manupulate and compare different sets or elements
#union combines 2 sets and removes duplicate data, intersection finds a common elements between 2 sets, difference finds elements available in 1 set and not the other
set1 = {1,2,3,4}
set2 = {4,5,6,7}

#union
union_set = set1.union(set2)
print(union_set)

#intersection
inter_set = set1.intersection(set2)
print(inter_set)

#Difference
diff_set = set1.difference(set2)
print(diff_set)











