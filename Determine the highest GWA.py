#create a txt file named gwa list
#open and read the files line by line
with open("Name and gwa.txt") as achiever:
    name_gwa = achiever.readlines()

#Input the highest grade a student can get
highest_grade = 5

#Using the split function, separate the name and gwa
for line in name_gwa:
    name,gwa = line.split(",")

    #Convert the gwa into a float
    gwa = float(gwa)

    #compare the gwa with the max grade
    if gwa < highest_grade:
        highest_grade = gwa

    #to output the name of the student with highest grade
        highest_student = name

#Print the highest grade
print("")
print("The highest GWA is:", highest_grade)
print("")
print("The name of the Highest student is:", highest_student)
print("")