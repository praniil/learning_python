import re

txt = "My name is Pranil Parajuli. Nickname nil"

x1 = re.findall("nil", txt) #returns a list of items in the order they are found
x2 = re.findall("americal", txt) #should return an empty list
print(x1, len(x1))
print(x2, len(x2))

search_obj = re.search("nil", txt)
print(search_obj.start(), search_obj.end())
