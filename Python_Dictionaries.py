village_school = {"name": "Boalia High School", "established": 1965, "total_teachers": 45, "total_students": 658}
school_details = {"address": "Boalia Bazar", "principal": "Sohidullah Kaisar", "founder": "Johir Raihan", "managing_committee": [{"name": "Sohrab Hossain", "age": 55, "occupation": "Retired person", "designation": "Chairman"}, {"name": "Raisul Islam", "age": 49, "occupation": "Businessman", "designation": "General Member"}, {"name": "Altaf Khan", "age": 33, "occupation": "Founder of Toto Company", "designation": "Vice Chairman"}, {"name": "Sohidul Islam", "age": 45, "occupation": "Businessman", "designation": "General Member"}]}

managing_committee_caniddates = [{"name": "Sultan Ahmed", "age": 43, "occupation": "Service Holder", "designation": "General Member"}, {"name": "Jamsed Khan", "age": 45, "occupation": "Doctor", "designation": "Vice Chairman"}, {"name": "Jahangir Talukder", "age": 47, "occupation": "Doctor", "designation": "Chairman"}, {"name": "Josim Uddin", "age": 38, "occupation": "Farmar", "designation": "Vice Chairman"}]


#output the data type of village_school
village_school = {"name": "Boalia High School", "established": 1965, "total_teachers": 45, "total_students": 658}
print(type(village_school)) 


#output the name of the above school
data =	{
  "name": "Boalia High School",
  "established": 1965,
  "total_teachers": 45,
  "total_students": 658
}
x = data["name"]
print(x)


#try to access "number_of_rooms" key of that school without getting any error
new = data.keys()
data["number_of_rooms"] = "65"
print(new) 
if "number_of_rooms" in data:
  print("For 'number_of_rooms' access are granted")


#change that schools establishment year and make it 1962
data["established"] = 1962
print(data)


#add school_details to village_school
village_school = {"name": "Boalia High School", "established": 1965, "total_teachers": 45, "total_students": 658}
school_details = {"address": "Boalia Bazar", "principal": "Sohidullah Kaisar", "founder": "Johir Raihan", "managing_committee": [{"name": "Sohrab Hossain", "age": 55, "occupation": "Retired person", "designation": "Chairman"}, {"name": "Raisul Islam", "age": 49, "occupation": "Businessman", "designation": "General Member"}, {"name": "Altaf Khan", "age": 33, "occupation": "Founder of Toto Company", "designation": "Vice Chairman"}, {"name": "Sohidul Islam", "age": 45, "occupation": "Businessman", "designation": "General Member"}]}
new_info=dict(village_school,**school_details)
print (new_info)


#check the length of village_school after adding school_details to it
print(len(new_info))


#add number_of_classrooms key with value 25 in village_school dictionary
if "number_of_classrooms" not in village_school:
    village_school["number_of_classrooms"] = "25"
print(village_school)


#check the data type of village_school
print(type(village_school)) 


#loop through all the values of village_school and check if any list type data found there if found print the key name
print(village_school)
for data4,data5 in village_school.items():
    if type(data5) == list:
      print(data4)

#output how many members are there in the managing committee
print(len(school_details['managing_committee']))


#check if 'Founder of Toto Company' exist in the managing committee if found then remove that person from the managing committee
for l, i in enumerate(school_details['managing_committee']):

     for j, k in i.items():
         if k == 'Founder of Toto Company':
             print('Yes')
             school_details['managing_committee'].pop(l)
             break

#output all the members occupation of the managing committee to check "Founder of Toto Company" is not there
print(school_details['managing_committee'])


#remove the last added item from the village_school (remember we've a built in function for that)
village_school.popitem()


#remove the founder of that school
del school_details["founder"]
print(school_details)


#set default value for founder key to "Robiul Islam"
village_school.setdefault('founder', 'Robiul Islam')


#check for a doctor in the 'managing_committee_candidates' list and make sure he wants to be the 'Vice Chairman' of that school if so then add that person to the managing_committe of that school
for i in managing_committee_caniddates:
     if i['occupation'] == 'Doctor' and i['designation'] == 'Vice Chairman':
         school_details['managing_committee'].append(i)


#output the member of managing_committee after update
print(village_school.get('managing_committee'))


#wipe out all the prperties of village_school and make it empty
village_school.clear()
print(village_school)

