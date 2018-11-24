#Write only 1st 10 odd numbers to the list
odd = []
for i in range(1,20):
    if i%2 !=0:
        odd.append(i)
print "Odd numbers are: ", odd
print len(odd)
