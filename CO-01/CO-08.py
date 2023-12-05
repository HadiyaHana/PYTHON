def replace(str1):
    str2 = str1[0]
    for i in range (1,len(str1)):
        if (str1[i] ==str1[0]):
            str2 = str2 + "$"
        else:
            str2 = str2 + str1[i]
    return str2

str1= input("Enter the string")
print(replace(str1))
