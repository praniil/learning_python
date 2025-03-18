from copy import deepcopy
#1st. reference of a list
list_a = ["pranil",1, 22, 33]
list_b = list_a #list_b and list_a points to the same list

list_b[0] = "NIL"
print(list_b)
print(list_a)

#copy of a list
cp_list_a = [1, 2, 3, 4, "pranil"]
cp_list_b = cp_list_a.copy()    #copies the lista to listb

#now they are different list
cp_list_b[len(cp_list_b) - 1] = "NIL"
print(cp_list_b)
print(cp_list_a)

#lets take an example of list that has list as element
#nested list
nes_list_a = [[1, 2, 3, 4, "Pranil Parajuli"], [1, 333, "second"]]
nes_list_b = nes_list_a.copy()
nes_list_b[0].append("appended")
print(nes_list_b)
print(nes_list_a)   #reflects to both the list but i did .copy()
#what happened is the outer list is copied but inderlying or nested list are simply the pointer to the same list

nes_list_b.append(["APPENDED A NEW LIST"])
print(nes_list_b)
print(nes_list_a)   #so here we can see that the outer list was copied but the elements of the list are simply the pointers to the prev list

#lets introduce deepcopy that copies everything 
dp_cp_list_a = [[1, 2 , 3, 4], ["pranil"]]
dp_cp_list_b = deepcopy(dp_cp_list_a)
dp_cp_list_b[0].append("hello")
print(dp_cp_list_b)
print(dp_cp_list_a)
#now the change in list b anywhere doesnt reflect on list a