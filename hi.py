
# path = "/home/joshuaehindero0/CODING./CLASSWORK FOLDER/Classes/hello_world.txt"


# Python will look for ↓this file
# with open('text_files/pi_dcigits.txt') as file_object:
#    contents = file_object.read()
#    print(contents)
# 'with' means that once the file has benn used, the file closes itself.

#   Relative path   ↑

# Absolute path             ↓

# with open("/home/joshuaehindero0/CODING./CLASSWORK FOLDER/Classes/hello_world.txt") as file_object:
#     contents = file_object.read()
#     print(contents)

# with open("/home/joshuaehindero0/CODING./CLASSWORK FOLDER/Classes/hello_world.txt") as file_object:
#     for line in file_object:
#       print(line.rstrip())

# String concatenation is the joining of two or more strings together using the (+) operator.

# with open("/home/joshuaehindero0/CODING./CLASSWORK FOLDER/Classes/hello_world.txt") as file_object:
#     lines = file_object.readlines()
#     pi_string = ''
#     for line in lines:
#         pi_string += line.rstrip()
# print(line.rstrip())
        
# text = "hello python"
# if "llo" in text:
#     print("It exists")



"""
Opened a file
read from a file (entire file)
read from a file (part of a file)
"""

# Writing to a file
with open("/home/joshuaehindero0/CODING./CLASSWORK FOLDER/Files & Exceptions/name_output.txt", "w") as file_object:
    file_object.write("I love python because it is so cool")

with open("/home/joshuaehindero0/CODING./CLASSWORK FOLDER/Files & Exceptions/name_output.txt", "a") as file_object:
    file_object.write("I also love python because it's super cool.")

with open("/home/joshuaehindero0/CODING./CLASSWORK FOLDER/Files & Exceptions/name_output.txt", "w") as file_object:
    file_object.write("I love being a programmer\n")
    file_object.write("I want everyone to have this feeling too\n")