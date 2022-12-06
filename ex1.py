#count the number of vowel in the string
name = input("Enter the string \n")
print ("The string you entered is: ", name)
count  = 0
for s in name:
    if (s=="a" or s=="e" or s=="i" or s=="o" or s=="u"):
        count +=1
print ("The number of vowels: ", count)
