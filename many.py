import random

#quick and dirty
times = int(input("How far out of your personal style will you go? "))

# Open files
Xfile = open('X.txt')
Yfile = open('Y.txt')

#create lists from files
X = [line.strip() for line in Xfile]
Y = [line.strip() for line in Yfile]

for num in range(0,times):
    s = "Todays challenge: "
    s = s + random.choice(X) + " and " + random.choice(Y)
    print (s)

print ("bye")
