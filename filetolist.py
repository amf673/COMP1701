

f = open("data1.txt", "r")
list_of_lines = []
for line in f: 
    list_of_lines.append(line)

i = 0
for line in list_of_lines: 
    i = i + 1
    print(f"{i}. {len(line)} {line[0:15]}...")
f.close()
