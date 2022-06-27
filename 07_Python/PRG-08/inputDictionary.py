import csv

secDictionary = {
    "First Name": input("First name? "),
    "Last Name": input("Last name? "),
    "Main Character": input("Main character name? "),
    "Age of main character": input("Age of main character? ")
}

# 'a'= append ipv 'w' =  write
# %s specifically is used to perform concatenation of strings together. It is used to incorporate another string within a string.
#with open('test1.csv', 'a') as f:
#   for key in secDictionary.keys():
#       f.write("%s, %s " % (key, secDictionary[key]))
#       f.write("\n")
# krijg de \n lines niet goed bij deze T-T want geen fieldnames (columns)

keys = secDictionary.keys()
filename = "test2.csv"

#open csvfile, append and go on the next line when "" is met
with open(filename, "a", newline="") as csvfile:
    #dictwriter heeft fieldnames 
    writer = csv.DictWriter(csvfile, fieldnames = keys)
    
    #writeheader() writes first line in csvfile as columnname
    writer.writeheader()
    #write the rows (values) into the csvfile
    writer.writerow(secDictionary) 