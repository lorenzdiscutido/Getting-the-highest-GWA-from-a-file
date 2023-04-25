#create a txt file named gwa list
#open and read the files line by line
with open("Name and gwa.txt") as achiever:
    name_gwa = achiever.readlines()

#Using the split function, separate the name and gwa
for line in name_gwa:
    name,gwa = line.split(",")