with open('Codingal.txt', 'w') as file:
    file.write("Today I am 12!")
file.close()

with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in thie file are:")
    for line in data:
        word = line.split()
        print(word)
file.close()