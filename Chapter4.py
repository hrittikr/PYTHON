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


collection = set()

print(type(collection))
