

f = open("data1.txt", "r")
output_file = open("sarcasm.txt", "w")

for line in f:
    sarcastic_line = ""
    i = 0
    for ch in line: 
        if i % 2 == 0:
            sarcastic_line = sarcastic_line + ch.upper()
        else: 
            sarcastic_line = sarcastic_line + ch.lower()
        i = i + 1
    output_file.write(sarcastic_line)
    
f.close()
output_file.close()

