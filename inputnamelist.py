name_list = []
maxLengthList = 10
while len(name_list) < maxLengthList:
     names = input(" write a name:")
     if names not in name_list:
        name_list.append(names)

print("that's the given names")
print(", ".join(name_list))
