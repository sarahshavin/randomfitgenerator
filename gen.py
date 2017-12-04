import random

'''
People wake up every morning and with no idea what to wear.

They want to dress well, yet different:
- Funky socks?
- Distracting earrings?
- A graphic tee under my professional blazer?

This generation script challenges you to dress weirder.
'''

# Open files
Xfile = open('X.txt')
Yfile = open('Y.txt')

#create lists from files
X = [line.strip() for line in Xfile]
Y = [line.strip() for line in Yfile]

s = "Todays challenge: "
s = s + random.choice(X) + " and " + random.choice(Y)
print (s)
