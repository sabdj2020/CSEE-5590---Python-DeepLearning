# create two lists
# list of weight in LBs
w_LB = []
# list of weight in KGs
w_KG = []

# enter the number of students
num_stu = int(input("How many students in the class : "))
for st in range(num_stu):
    w = float(input("Enter the weight of student %s in LBS please : " %st))
# add the weight to the weight list in lbs
    w_LB.append(w)
    w = w * 0.453592
# round the weight for only two and add it to the weight list kg
    w_KG.append(round(w, 2))
# print the students weight list in lbs
print("this is the list of students weight in lbs")
print(w_LB)

# print the students weight list in kilograms
print("this is the list of students weight in kilograms")
print(w_KG)
print ("hello")