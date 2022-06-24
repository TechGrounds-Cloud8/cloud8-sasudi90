import csv

firstName = input("First name? ")
lastName = input("Last name? ")
mainChar = input("Main character name? ")
storageChar = input("Storage character name? ")

secDictionary = {
    "First Name": firstName,
    "Last Name": lastName,
    "Main Character": mainChar,
    "Bank Character": storageChar
}

#for key in secDictionary:
#    print(key,": ", secDictionary[key])

with open('test1.csv', 'w') as f:
    for key in secDictionary.keys():
        f.write("%s, %s\n" % (key, secDictionary[key]))