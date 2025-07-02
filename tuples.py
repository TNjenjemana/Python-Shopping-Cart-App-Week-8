# tuple is a collection of order ellements
#similar to list, but unchangable/immutable
#tuples are usefull for representing fixed collection of items
# tuples are order and unchangable,but also allow duplicates

my_tuple = (1,2,3,4,5)# you access individual elements of tuple by indexing.Indexing starts at zero
print(my_tuple)
print(my_tuple[3])
print(my_tuple[0])
print(my_tuple[-1])# -1 index always prints out the last index value.this is true for lists and tuples.

tuple1 = (1,2,3)
tuple2 = (4,5,6)

conc_tuple = tuple1 + tuple2 #adding tuple1 and tuple2

print(conc_tuple)

rep_tuple = tuple2*3 # repeat tuples.

print(rep_tuple)