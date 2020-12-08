# my_file = open("fruits.txt")
# my_file.close()
# print(my_file.read())
# with open("fruits.txt") as my_file:
#     content = my_file.read()
#
# print(content)
# now writing concept
with open("vegetables.txt", "w") as file:
    file.write("i am good how are you?")