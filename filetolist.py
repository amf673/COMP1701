

f = open("data.txt", "r")
list_of_lines = []
for line in f: 
    list_of_lines.append(line)

print(list_of_lines)
f.close()
