new_file = open('new_file.txt', 'x')
new_file.close()

import os
print("Checl=king if my_file exists or not. Pleae hold.")
if os.path.exists("my_file.txt"):
    os.remove('my_file.txt')
else:
    print("This file does not exist.")

my_file = open('my_file.txt', 'w')
print("Hi I am Anaira. I am 12 years old.")
my_file.close()

os.remove("my_file.txt")

os.rmdir('To be deleted')