tuple_a = "pranil", "parajuli"
print(type(tuple_a))
#tuple's element are immutable
print(tuple_a[0]) #ordered
# tuple_a[0] = "NIL"  #trying to mutate immutable error
print(tuple_a[0])
print(tuple_a)

#list we can mutate the element
list_a = ["pranil", "NIL", "parajuli"]
print(list_a[0])
list_a[0] = "Pranil Parajuli NIL"   #mutable
print(list_a[0])