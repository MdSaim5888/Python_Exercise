students1 = {"shaon", "sufian", "sohrab", "risat", "sohrab", "shaon", "sohan", "romiz"}
students2 = {"kobir", "shaon", "rakib"}

a = {8, 4, 3, 3, 2, 7, 5}
b = {1, 4, 9, 20, 34}



#check the data type of students
print(type(students1)) 
print(type(students2)) 


#check the length of students
print(len(students1)) 
print(len(students2)) 


#add "sweety" to students
students1.add("sweety")
students2.add("sweety")
print(students1)
print(students2)


#remove "risat" from students
students1.remove("risat")
print(students1)


#try to safely remove "raihan" from students without facing any error
students1.add("raihan")
print(students1)
students1.remove("raihan")
print(students1)



#add students2 to students1
students2.update(students1)
print(students2)


#check is students2 is the subset of student1
subset = students2.issubset(students1)
print(subset)


#check is students1 is the superset of student2
superset = students1.issuperset(students2)
print(superset)


#clear student1
students1.clear()
students2.clear()
print(students1)
print(students2)


#print all the combined items of student1 and student2, without any duplication (without making any permanent change)
students1 = {"shaon", "sufian", "sohrab", "risat", "sohrab", "shaon", "sohan", "romiz"}
students2 = {"kobir", "shaon", "rakib"}
students=students1.symmetric_difference(students2)
print(students)


#print all the combined items of student1 and student2, with all common values of them (without making any permanent change)
z = students1.intersection(students2) 
print(z)


#print all the combined items of student1 and student2, with all uncommon values of them (without making any permanent change)
students1 = {"shaon", "sufian", "sohrab", "risat", "sohrab", "shaon", "sohan", "romiz"}
students2 = {"kobir", "shaon", "rakib"}
students1.symmetric_difference_update(students2) 
print(students1)


