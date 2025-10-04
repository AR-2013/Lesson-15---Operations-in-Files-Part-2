import os
print("Checl=king if my_file exists or not. Pleae hold.")
if os.path.exists("Homework3.txt"):
    os.remove('Homework3.txt')
else:
    print("This file does not exist.")

my_file = open('Homework3.txt', 'w')
print("Hi I am Anaira. I am 12 years old.")
my_file.close()

os.remove("Homework3.txt")