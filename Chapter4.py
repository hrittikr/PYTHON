#Dictionary & Sets


info = {
    "key" : "value",
    "name" : "Hrittik",
    "age" : 22,
    "city" : "Patna",
    "is_adult" : True,
    "subjects" : ["maths", "science", "english"],
    "marks" : 94.3,
    32 : 56
    }

# info["name"] = "Raushan"
# info["surname"] = "ashish"
# print(info["name"])
# print(info["age"])
# print(info["city"])
# print(info["is_adult"])
# print(info["surname"])
# print(info)
# print(info["grace"]) #this will give an error because there is no key named "grace" in the dictionary

# null_dict ={}
# null_dict["name"] = "Hrittik"
# print(null_dict)


#nested dictionaries

student ={
    "name" : "Hrittik",
    "subjects" : {
        "physics" : 90,
        "chemistry" : 85,
        "maths" : 95
    }
}
# print(student["subjects"]["physics"])

# print(list(student.keys()))
# print(list(student.values()))
# print(list(student.items()))
# print(student.get("name11"))
# print(student.get("subjects"))
# print(student["subjects"]["physics"])
# print(student.get("subjects"))
# print("before")

# student.update({"name" : "ashish"})
# print(student) 





# collection = {1, 2, 4, 4, "Hello", 6, "hrittik", 8, 9}

# print(collection)
# print(len(collection))
# print(type(collection))


# collection = set()

# print(type(collection))

# set1 = {3,4,5,7,5,7,8}
# # set1.add(9)
# # set1.remove(4)
# set1.clear()
# print(set1)
# print(len(set1))
# print(type(set1))

# set2 = {1, 2, 3, 4, 5}
# set3 = {4, 5, 6, 7, 8}

# union_set = set2.union(set3)

# print(union_set)


# inter_set = set2.intersection(set3)
# print(inter_set)





#practice question

# a = {
#     "table" : ["a piece of furniture", "list of facts & figures" ],
#     "cat" : "a small animal"
# }

# print(a)

# # you are givenn a list of subjects for students. Assume one clasroom is required for 1 subject. How many classrooms are needed by all students.
# subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# print(len(subjects))

# marks = {}
# sub1 = int(input("Marks in subject 1: "))
# sub2 = int(input("Marks in subject 2: "))
# sub3 = int(input("Marks in subject 3: "))

# dict = {
#     "subject1" : sub1,
#     "subject2" : sub2,
#     "subject3" : sub3
# }
# print(dict)



# set = {9 , "9.0"}
# print(set)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)