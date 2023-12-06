dict1 = {1: "hi", 2: "how", 3: "are", 4: "you"}
print("Dictionary:", dict1)

reversed_dict1= {}
l = len(dict1)

for i in range(1, l + 1):
    reversed_dict1[i] = dict1[l-i+1]

print("Reversed Dictionary:", reversed_dict1)
