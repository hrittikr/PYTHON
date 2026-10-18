#list & tuple

# marks =[56, "arjun", 78, "priya", 90, 100]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1:4])
# print(len(marks))
# marks[1]="hrittik"
# print(marks)

# marks.append(99)
# print(marks)



# list1 = [1, 8, 3, 7, 5]
# print(list1.append(9))
# print(list1.sort())
# print(list1)

# print(list1.sort(reverse=True))
# print(list1)


# list2 = ["banana","apple","mango"]
# # print(list2.sort())
# print(list2.sort(reverse=True))
# print(list2)


# list3 = [1, 2, 3, 4, 5]
# list3.insert(2, 99)
# print(list3)


# list4 = [1, 2, 3, 3, 5]
# # list4.remove(3)
# # print(list4)

# list4.pop(1)
# print(list4)




# tup = (2, 4, 5, 9)
# print(type(tup))
# print(tup[0])
# print(tup[1:3])

# tup=(1,)
# print(tup)
# print(type(tup))

# tup = (2, 4, 5, 9)
# print(tup.count(4))


#practise questions
# #WAP to ask the user to enter three movie names and store them in a list and print the list.
# a = input("Enter the first movie name:")
# b = input("Enter the second movie name:")
# c = input("Enter the third movie name:")

# movie =[a, b, c]
# print(movie)

# a = input("Enter the 1st element:")
# b = input("Enter the 2nd element:")
# c = input("Enter the 3rd element:")
# d = input("Enter the 4th element:")

# list = [a, b, c, d]
# if(a==d and b==c):
#     print("it is a palindrome")
#     print(list)
# else:
#     print("not a palinrome")
#     print(list)
    
    
# #method2
# a = input("1st Element:")
# b = input("2nd Element:")
# c = input("3rd Element:")
# d = input("4th Element:")
# e = input("5th Element:")

# list1 = [a, b, c, d ,e]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")
#     print(list1)
# else:
#     print("Not Palindrome")
    

# #WAP to count the number of students with the "A" grade in the following tuple
# tup = ("C", "D", "A", "A", "B", "B", "A")
# print(tup.count("A"))


# store the above values in a list & sort them from "A"to "D"
tup1 = ["C", "D", "A", "A", "B", "B", "A"]
tup1.sort()
print(tup1)