#For Loop
print "=================================="
names = ("darwin","einstein","bharathiar","tolstoy")
for i in names:
    print i
print "=================================="
for i in range(len(names)):#use of range
    print i,names[i]
print "=================================="

for i,j in enumerate(names):#use of enumerate
    print i,j
