#finding the amount of "bob" in s

s = "fdjsabobjfdklsabobjfkdsabob"

counter = 0

for i in range(1,len(s)-1):
    if s[i-1:i+2] == "bob":
        counter += 1

print counter



