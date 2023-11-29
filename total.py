f = open("data_num.txt", "r")
total = 0
for line in f:
    total = total + int(line)
    
print(total)
f.close()

